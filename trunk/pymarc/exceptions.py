class pymarcException( Exception ):
    pass

class RecordLengthInvalid( pymarcException):
    def __str__( self ):
        return( "invalid record length in first 5 bytes of record" )

class RecordLeaderInvalid( pymarcException ):
    def __str__ ( self ):
        return "Unable to extract record leader"

class RecordDirectoryInvalid( pymarcException ):
    def __str__( self ):
        return "Invalid directory"

class NoFieldsFound( pymarcException ):
    def __str__ ( self ):
        return "Unable to locate fields in record data"

class BaseAddressInvalid( pymarcException ):
    def __str__ ( self ):
        return "Base address exceeds size of record"

class WriteNeedsRecord( pymarcException ):
    def __str__( self ):
        return "write requires a pymarc.Record object as an argument"

class NoActiveFile( pymarcException ):
    def __str__( self ):
        return "There is no active file to write to in call to write"
