# This file is part of pymarc. It is subject to the license terms in the
# LICENSE file found in the top-level directory of this distribution and at
# https://opensource.org/licenses/BSD-2-Clause. pymarc may be copied, modified,
# propagated, or distributed according to the terms contained in the LICENSE
# file.

"""Exceptions for pymarc."""


class PymarcException(Exception):
    """Base pymarc Exception."""

    pass


class RecordLengthInvalid(PymarcException):
    """Invalid record length."""

    def __str__(self):
        return "Invalid record length in first 5 bytes of record"


class RecordLeaderInvalid(PymarcException):
    """Unable to extract record leader."""

    def __str__(self):
        return "Unable to extract record leader"


class RecordDirectoryInvalid(PymarcException):
    """Invalid directory."""

    def __str__(self):
        return "Invalid directory"


class NoFieldsFound(PymarcException):
    """Unable to locate fields in record data."""

    def __str__(self):
        return "Unable to locate fields in record data"


class BaseAddressInvalid(PymarcException):
    """Base address exceeds size of record."""

    def __str__(self):
        return "Base address exceeds size of record"


class BaseAddressNotFound(PymarcException):
    """Unable to locate base address of record."""

    def __str__(self):
        return "Unable to locate base address of record"


class WriteNeedsRecord(PymarcException):
    """Write requires a pymarc.Record object as an argument."""

    def __str__(self):
        return "Write requires a pymarc.Record object as an argument"


class NoActiveFile(PymarcException):
    """There is no active file to write to in call to write."""

    def __str__(self):
        return "There is no active file to write to in call to write"


class FieldNotFound(PymarcException):
    """Record does not contain the specified field."""

    def __str__(self):
        return "Record does not contain the specified field"


class BadSubfieldCodeWarning(Warning):
    """Warning about a non-ASCII subfield code."""

    pass


class BadLeaderValue(PymarcException):
    """Error when setting a leader value."""

    pass
