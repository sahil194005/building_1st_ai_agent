from schemas import *
from tools import *
# from tool_functions import */


def execute_tool(tool_name, arguments):

    if tool_name == "calculate_return_on_investment":
        data = ROIInput(**arguments)
        return calculate_return_on_investment(data.investment, data.return_amount)

    elif tool_name == "add_numbers":
        data = AddNumbersInput(**arguments)
        return add_numbers(data.a, data.b)

    elif tool_name == "multiply_numbers":
        data = MultiplyNumbersInput(**arguments)
        return multiply_numbers(data.a, data.b)

    elif tool_name == "get_stock_price":
        data = StockPriceInput(**arguments)
        return get_stock_price(data.symbol)

    elif tool_name == "convert_currency":
        data = CurrencyConvertInput(**arguments)
        return convert_currency(data.amount, data.from_currency, data.to_currency)

    else:
        raise ValueError(f"Unknown tool: {tool_name}")
