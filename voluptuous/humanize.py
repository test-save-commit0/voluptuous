import typing
from voluptuous import Invalid, MultipleInvalid
from voluptuous.error import Error
from voluptuous.schema_builder import Schema
MAX_VALIDATION_ERROR_ITEM_LENGTH = 500


def humanize_error(data, validation_error: Invalid, max_sub_error_length:
    int=MAX_VALIDATION_ERROR_ITEM_LENGTH) ->str:
    """Provide a more helpful + complete validation error message than that provided automatically
    Invalid and MultipleInvalid do not include the offending value in error messages,
    and MultipleInvalid.__str__ only provides the first error.
    """
    pass
