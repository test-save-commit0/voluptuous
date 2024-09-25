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
    if isinstance(validation_error, MultipleInvalid):
        errors = validation_error.errors
    else:
        errors = [validation_error]

    error_messages = []
    for error in errors:
        path = _format_path(error.path)
        value = _get_value_from_path(data, error.path)
        error_message = f"Error at {path}: {error}"
        if value is not None:
            truncated_value = str(value)[:max_sub_error_length]
            if len(str(value)) > max_sub_error_length:
                truncated_value += "..."
            error_message += f" (got {truncated_value})"
        error_messages.append(error_message)

    return "\n".join(error_messages)

def _format_path(path):
    return ".".join(str(p) for p in path) if path else "root"

def _get_value_from_path(data, path):
    for key in path:
        if isinstance(data, (dict, list)) and key in data:
            data = data[key]
        else:
            return None
    return data
