from constants import *
from exceptions import * 

class Field( object ):

    def __init__( self, tag, indicators=[], subfields=[], data='' ):
        """
        Field() pass in the field tag, indicators and subfields for the tag.
 
            field = Field( \
                tag = '245', 
                indicators = ['0','1'],
                subfields = [ \
                    'a', 'The pragmatic programmer : ',
                    'b', 'from journeyman to master /', 
                    'c', 'Andrew Hunt, David Thomas.' ]

        If you want to create a control field you don't pas in the indicators
        and use a data parameter rather than a subfields parameter:

            field = Field( tag='001', data='fol05731351' )

        """
        tag = "%03s" % tag
        if ( tag < '010' ):
            self.tag = tag
            self.data = data
        else: 
            self.tag = tag 
            self.indicators = indicators
            self.indicator1 = indicators[0] 
            self.indicator2 = indicators[1] 
            self.subfields = subfields 

    def __iter__(self):
        self.__pos = 0
        return self

    def __str__( self ):
        """
        A Field object in a string context will return the tag, indicators
        and subfield as a string. This follows MARCMaker format; see [1]
        and [2] for further reference. Special character mnemonic strings
        have yet to be implemented (see [3]), so be forewarned. Note also
        for complete MARCMaker compatibility, you will need to change your
        newlines to DOS format ('\r\n').
        
        [1] http://www.loc.gov/marc/makrbrkr.html#mechanics
        [2] http://search.cpan.org/~eijabb/MARC-File-MARCMaker/
        [3] http://www.loc.gov/marc/mnemonics.html
        """
        if ( self.isControlField() ): 
            text = "=%s  %s" % ( self.tag, self.data.replace(' ','\\') )
        else:
            text = "=%s  " % ( self.tag )
            for indicator in self.indicators:
                if indicator in (' ','\\'):
                    text += "\\"
                else:
                    text += "%s" % indicator
            for subfield in self:
                text += ("$%s%s" % subfield) 
        return text

    def __getitem__( self, subfield ):
        """
        Retrieve the first subfield with a given subfield code in a field:

            field['a']

        Handy for quick lookups.
        """
        subfields = self.getSubfields( subfield )
        if len(subfields) > 0: return subfields[0]
        return None

    def next( self ):
        while self.__pos < len(self.subfields):
            subfield = ( self.subfields[ self.__pos ], \
                self.subfields[ self.__pos+1 ] )
            self.__pos += 2
            return subfield
        raise StopIteration

    def value( self ):
        """
        Returns the field as a string without tag, indicators, and 
        subfield indicators.
        """
        if self.isControlField():
            return self.data
        string = ""
        for subfield in self:
            string += subfield[1]
        return string

    def getSubfields( self, *codes ):
        """
        getSubfields() accepts one or more subfield codes and will return a list
        of subfield values.  The order of the subfield values in the list 
        will be the order that they appear in the field.

            print field.getSubfields( 'a' )

            print field.getSubfields( 'a', 'b', 'z' )
        """
        values = []
        for subfield in self:
            if subfield[0] in codes:
                values.append( subfield[1] )
        return values 

    def addSubfield( self, code, value ):
        """
        Adds a subfield code/value pair to the field.

            field.addSubfield('u', 'http://www.loc.gov')
        """
        self.subfields.append(code)
        self.subfields.append(value)

    def isControlField( self ):
        """
        returns true or false if the field is considered a control field.
        Control fields lack indicators and subfields.
        """
        if self.tag < '010': 
            return True
        return False

    def asMARC21( self ):
        """
        used during conversion of a field to raw marc
        """
        if self.isControlField():
            return self.data + END_OF_FIELD
        marc = str(self.indicator1) + str(self.indicator2)
        for subfield in self:
            marc += SUBFIELD_INDICATOR + subfield[0] + subfield[1]
        return marc + END_OF_FIELD

    def formatField( self ):
        """
        Returns the field as a string without tag, indicators, and subfield indicators. Like pymarc.Field.value(), but prettier (adds spaces, formats subject headings).
        """
        if self.isControlField(): return self.data
        fielddata = ''
        for subfield in self:
            if not self.isSubjectField():
                fielddata += ' %s' % subfield[1]
            else:
                if subfield[0] not in ('v','x','y','z'):
                    fielddata += ' %s' % subfield[1]
                else: fielddata += ' -- %s' % subfield[1]
        return fielddata.strip()
    
    def isSubjectField( self ):
        """
        returns True or False if the field is considered a subject field - used by formatField
        """
        if self.tag.startswith('6'): return True
        return False
