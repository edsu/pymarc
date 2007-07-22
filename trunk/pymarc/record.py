from exceptions import * 
from constants import *
from field import * 
from types import *
import string
import re


class Record( object ):
    """
    Record 

    A class for representing a MARC record. Each Record object is made up of
    multiple Field objects. You'll probably want to look at the docs for Field
    to see how to fully use a Record object.

    Basic usage:

        field = Field( \
            tag = '245', 
            indicators = ['0','1'],
            subfields = [ \
                'a', 'The pragmatic programmer : ',
                'b', 'from journeyman to master /', 
                'c', 'Andrew Hunt, David Thomas.' ]

        record.addField( field )

    Or creating a record from a chunk of MARC in transmission format:

        record = Record( data=chunk )

    Or getting a record as serialized MARC21.

        raw = record.asMARC21()

    You'll normally want to use a MARCReader object to iterate through 
    MARC records in a file.  
    """

    def __init__( self, data='' ):
        self.leader = (' '*10) + '22' + (' '*8) + '4500'
        self.fields = list()
        self.pos = 0
        if len(data) > 0:
            ok = self.decodeMARC( data )

    def __str__( self ):
        """
        In a string context a Record object will return a prettified version
        of the record in MARCMaker format. See the docstring for Field.__str__
        for more information.
        """
        # join is significantly faster than concatenation
        text = "=LDR  %s\n" % self.leader
        text += string.join( map( str, self.fields ), "\n" )
        text += '\n'
        return text

    def __getitem__( self, tag ):
        """
        Allows a shorthand lookup by tag:
        
            record["245"]

        """
        fields = self.getFields( tag )
        if len(fields) > 0: return fields[0]
        return None

    def __iter__( self ):
        self.__pos = 0
        return self

    def next(self):
        if self.__pos >= len( self.fields ):
            raise StopIteration
        self.__pos += 1 
        return self.fields[ self.__pos-1 ]

    def addField( self, *fields ):
        """
        addField() will add pymarc.Field objects to a Record object.
        Optionally you can pass in multiple fields.
        """
        self.fields.extend(fields)

    def getFields( self, *args ):
        """
        When passed a tag ( '245' ) getFields() will return a list of all the 
        fields in a record with a given tag. 

            title = record.getFields( '245' )
        
        If no fields with the specified 
        tag are found then an empty list is returned. If you are interested
        in more than one tag you can pass in a list:

            subjects = record.getFields( '600', '610', '650' ) 

        If no tag is passed in to fields() a list of all the fields will be 
        returned.
        """
        if (len(args) == 0):
            return self.fields

        return [f for f in self.fields if f.tag in args]

    def decodeMARC( self, marc ):
        """
        decodeMARC() accepts a MARC record in transmission format as a
        a string argument, and will populate the object based on the data
        found. The Record constructor actually uses decodeMARC() behind
        the scenes when you pass in a chunk of MARC data to it.

        """

        # extract record leader
        self.leader = marc[ 0 : LEADER_LEN ]
        if len( self.leader ) != LEADER_LEN: raise RecordLeaderInvalid

        # extract the byte offset where the record data starts
        baseAddress = int( marc[ 12 : 17 ] )
        if baseAddress <= 0: raise BaseAddressNotFound
        if baseAddress >= len( marc ): raise BaseAddressInvalid

        # extract directory, baseAddress-1 is used since the 
        # director ends with an END_OF_FIELD byte
        directory = marc[ LEADER_LEN : baseAddress-1 ]

        # determine the number of fields in record
        if len(directory) % DIRECTORY_ENTRY_LEN <> 0:
            raise RecordDirectoryInvalid
        numFields = len( directory ) / DIRECTORY_ENTRY_LEN 
        
        # add fields to our record using directory offsets
        fieldNum = 0
        while ( fieldNum < numFields  ):
            entryStart = fieldNum * DIRECTORY_ENTRY_LEN
            entryEnd = entryStart + DIRECTORY_ENTRY_LEN
            entry = directory[ entryStart : entryEnd ]
            entryTag = entry[ 0 : 3 ]
            entryLength = int( entry[ 3 : 7 ] )
            entryOffset = int( entry[ 7 : 12 ] )
            entryData = marc[ baseAddress + entryOffset : 
                baseAddress + entryOffset + entryLength - 1 ]

            if entryTag < '010':
                field = Field( tag=entryTag, data=entryData )
            else:
                subfields = list()
                subs = entryData.split( SUBFIELD_INDICATOR )
                i1 = subs[0][0]
                i2 = subs[0][1]
                for subfield in subs[1:]:
                    if len(subfield) == 0: continue
                    code = subfield[0]
                    data = subfield[1:]
                    subfields.append( code )
                    subfields.append( data )
                field = Field( 
                    tag = entryTag, 
                    indicators = [ i1, i2 ], 
                    subfields = subfields )

            self.addField( field )
            fieldNum += 1

        if fieldNum == 0: raise NoFieldsFound 

    def asMARC21( self ):
        """
        returns the record serialized as MARC21
        """
        fields = '' 
        directory = '' 
        offset = 0

        # build the directory
        # each element of the directory includes the tag, the byte length of 
        # the field and the offset from the base address where the field data
        # can be found
        for field in self.fields:
            fieldData = field.asMARC21()
            fields += fieldData
            directory += "%03d%04d%05d" % (int(field.tag),len(fieldData),offset)
            offset += len( fieldData )

        # directory ends with an end of field
        directory += END_OF_FIELD

        # field data ends with an end of record
        fields += END_OF_RECORD

        # the base address where the directory ends and the field data begins
        baseAddress = LEADER_LEN + len(directory)

        # figure out the length of the record 
        recordLength = baseAddress + len(fields)

        # update the leader with the current record length and base address
        # the lengths are fixed width and zero padded
        self.leader = "%05d%s%05d%s" % \
            ( recordLength, self.leader[5:12], baseAddress, self.leader[17:] )
        
        # return the encoded record
        return self.leader + directory + fields 

    def title( self ):
        """
        Returns the title of the record (245 $a an $b).
        """
        title = None 
        try:
            title = self['245']['a'] 
            title += self['245']['b'] 
        except TypeError, e: 
            pass 
        return title

    def isbn( self ):
        """
        Returns an ISBN if appropriate. If not present None will
        be returned.
        """
        isbn = None 
        try: 
            # if anyone ever cares alot about performance 
            # this compilation could be moved out and compiled once
            isbnPattern = re.compile( '^([0-9A-Za-z]+)' )
            isbn = isbnPattern.match( self["020"]["a"] ).group(1)
        except Exception, e:
            pass
        return isbn

    def author( self ):
        if self['100']:
            return self['100'].formatField()
        elif self['110']:
            return self['110'].formatField()
        elif self['111']:
            return self['111'].formatField()
        return None
    
    def uniformtitle( self ):
        if self['130']:
            return self['130'].formatField()
        elif self['240']:
            return self['240'].formatField()
        return None

    def subjects( self ):
        """
        Note: Fields 690-699 are considered "local" added entry fields but
        occur with some frequency in OCLC and RLIN records.
        """
        subjlist = self.getFields (
            '600', '610', '611', '630', '648', '650', '651', '653', '654',
            '655', '656', '657', '658', '662', '690', '691', '696', '697',
            '698', '699'
          )
        return subjlist
    
    def addedentries( self ):
        """
        Note: Fields 790-799 are considered "local" added entry fields but
        occur with some frequency in OCLC and RLIN records.
        """
        aelist = self.getFields (
            '700', '710', '711', '720', '730', '740', '752', '753', '754',
            '790', '791', '792', '793', '796', '797', '798', '799'
          )
        return aelist
    
    def location( self ):
        loc = self.getFields('852')
        return loc

    def notes( self ):
        # todo
        pass

    def publisher( self ):
        # todo
        pass

    def pubyear( self ):
        # todo
        pass
