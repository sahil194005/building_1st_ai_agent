from schemas import *
from tools import TOOL_FUNCS



from pydantic import ValidationError


def validate_arguments(tool_name: str, arguments: dict):
    """Return a validated Pydantic model instance for the given tool.

    Raises:
        ValueError: when the tool is not recognized.
        ValidationError: when the arguments do not match the schema.
    """
    if tool_name == "calculate_return_on_investment":
        return ROIInput(**arguments)
    elif tool_name == "add_numbers":
        return AddNumbersInput(**arguments)
    elif tool_name == "multiply_numbers":
        return MultiplyNumbersInput(**arguments)
    elif tool_name == "get_stock_price":
        return StockPriceInput(**arguments)
    elif tool_name == "convert_currency":
        return CurrencyConvertInput(**arguments)
    else:
        raise ValueError(f"Unknown tool: {tool_name}")


def validate_and_execute(tool_name: str, arguments: dict):
    """Validate arguments and run the corresponding tool function.

    Returns the result of the tool or raises an error if validation fails.
    """
    validated = validate_arguments(tool_name, arguments)
    func = TOOL_FUNCS.get(tool_name)
    if func is None:
        raise ValueError(f"No implementation for tool '{tool_name}'")

    # Pydantic models expose a dict of field values
    return func(**validated.dict())


# keep execute_tool alias for backwards compatibility
execute_tool = validate_and_execute
