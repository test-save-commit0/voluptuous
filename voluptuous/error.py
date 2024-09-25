import typing


class Error(Exception):
    """Base validation exception."""


class SchemaError(Error):
    """An error was encountered in the schema."""


class Invalid(Error):
    """The data was invalid.

    :attr msg: The error message.
    :attr path: The path to the error, as a list of keys in the source data.
    :attr error_message: The actual error message that was raised, as a
        string.

    """

    def __init__(self, message: str, path: typing.Optional[typing.List[
        typing.Hashable]]=None, error_message: typing.Optional[str]=None,
        error_type: typing.Optional[str]=None) ->None:
        Error.__init__(self, message)
        self._path = path or []
        self._error_message = error_message or message
        self.error_type = error_type

    def __str__(self) ->str:
        path = ' @ data[%s]' % ']['.join(map(repr, self.path)
            ) if self.path else ''
        output = Exception.__str__(self)
        if self.error_type:
            output += ' for ' + self.error_type
        return output + path


class MultipleInvalid(Invalid):

    def __init__(self, errors: typing.Optional[typing.List[Invalid]]=None
        ) ->None:
        self.errors = errors[:] if errors else []

    def __repr__(self) ->str:
        return 'MultipleInvalid(%r)' % self.errors

    def __str__(self) ->str:
        return str(self.errors[0])


class RequiredFieldInvalid(Invalid):
    """Required field was missing."""


class ObjectInvalid(Invalid):
    """The value we found was not an object."""


class DictInvalid(Invalid):
    """The value found was not a dict."""


class ExclusiveInvalid(Invalid):
    """More than one value found in exclusion group."""


class InclusiveInvalid(Invalid):
    """Not all values found in inclusion group."""


class SequenceTypeInvalid(Invalid):
    """The type found is not a sequence type."""


class TypeInvalid(Invalid):
    """The value was not of required type."""


class ValueInvalid(Invalid):
    """The value was found invalid by evaluation function."""


class ContainsInvalid(Invalid):
    """List does not contain item"""


class ScalarInvalid(Invalid):
    """Scalars did not match."""


class CoerceInvalid(Invalid):
    """Impossible to coerce value to type."""


class AnyInvalid(Invalid):
    """The value did not pass any validator."""


class AllInvalid(Invalid):
    """The value did not pass all validators."""


class MatchInvalid(Invalid):
    """The value does not match the given regular expression."""


class RangeInvalid(Invalid):
    """The value is not in given range."""


class TrueInvalid(Invalid):
    """The value is not True."""


class FalseInvalid(Invalid):
    """The value is not False."""


class BooleanInvalid(Invalid):
    """The value is not a boolean."""


class UrlInvalid(Invalid):
    """The value is not a URL."""


class EmailInvalid(Invalid):
    """The value is not an email address."""


class FileInvalid(Invalid):
    """The value is not a file."""


class DirInvalid(Invalid):
    """The value is not a directory."""


class PathInvalid(Invalid):
    """The value is not a path."""


class LiteralInvalid(Invalid):
    """The literal values do not match."""


class LengthInvalid(Invalid):
    """The value has an invalid length."""


class DatetimeInvalid(Invalid):
    """The value is not a formatted datetime string."""


class DateInvalid(Invalid):
    """The value is not a formatted date string."""


class InInvalid(Invalid):
    """The value is not in the required collection."""


class NotInInvalid(Invalid):
    """The value is in a collection it should not be in."""


class ExactSequenceInvalid(Invalid):
    """The sequence does not match exactly."""


class NotEnoughValid(Invalid):
    """The value did not pass enough validations."""
    def __init__(self, msg: str, min_valid: int, actual_valid: int, path: typing.Optional[typing.List[typing.Hashable]] = None):
        super().__init__(msg, path)
        self.min_valid = min_valid
        self.actual_valid = actual_valid


class TooManyValid(Invalid):
    """The value passed more than expected validations."""
    def __init__(self, msg: str, max_valid: int, actual_valid: int, path: typing.Optional[typing.List[typing.Hashable]] = None):
        super().__init__(msg, path)
        self.max_valid = max_valid
        self.actual_valid = actual_valid
