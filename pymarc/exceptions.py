"Exceptions for pymarc."

class PymarcException(Exception):
    pass

class RecordLengthInvalid(PymarcException):
    def __str__(self):
        return "Invalid record length in first 5 bytes of record"

class RecordLeaderInvalid(PymarcException):
    def __str__(self):
        return "Unable to extract record leader"

class RecordDirectoryInvalid(PymarcException):
    def __str__(self):
        return "Invalid directory"

class NoFieldsFound(PymarcException):
    def __str__(self):
        return "Unable to locate fields in record data"

class BaseAddressInvalid(PymarcException):
    def __str__(self):
        return "Base address exceeds size of record"

class BaseAddressNotFound(PymarcException):
    def __str__(self):
        return "Unable to locate base address of record"

class WriteNeedsRecord(PymarcException):
    def __str__(self):
        return "Write requires a pymarc.Record object as an argument"

class NoActiveFile(PymarcException):
    def __str__(self):
        return "There is no active file to write to in call to write"

class FieldNotFound(PymarcException):
    def __str__(self):
        return "Record does not contain the specified field"
