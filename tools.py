tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate_return_on_investment",
            "description": "Calculate ROI percentage from investment and return amount. Use when user asks about profit percentage or investment performance.",
            "parameters": {
                "type": "object",
                "properties": {
                    "investment": {
                        "type": "number",
                        "description": "Initial money invested",
                    },
                    "return_amount": {
                        "type": "number",
                        "description": "Final value received after investment",
                    },
                },
                "required": ["investment", "return_amount"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "add_numbers",
            "description": "Add two numbers and return the sum. Use when the user asks for arithmetic addition of two values.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "First addend"},
                    "b": {"type": "number", "description": "Second addend"},
                },
                "required": ["a", "b"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "multiply_numbers",
            "description": "Multiply two numbers together. Use when the user asks for a product or scaling of values.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "First factor"},
                    "b": {"type": "number", "description": "Second factor"},
                },
                "required": ["a", "b"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "subtract_numbers",
            "description": "Subtract two numbers and return the difference. Use when the user asks for arithmetic subtraction of two values.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "Minuend"},
                    "b": {"type": "number", "description": "Subtrahend"},
                },
                "required": ["a", "b"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_percentage_difference",
            "description": "Calculate the percentage difference between two values. Use when the user asks to compare two quantities and find the relative change.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "First value"},
                    "b": {"type": "number", "description": "Second value"},
                },
                "required": ["a", "b"],
            },
        },
    },
    
    {
        "type": "function",
        "function": {
            "name": "get_stock_price",
            "description": "Get the  price of a stock . Use when the user asks for the  price of a stock like AAPL or TSLA.",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Ticker symbol of the stock",
                    },
                },
                "required": ["symbol"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "convert_currency",
            "description": "Convert an amount from one currency to another using a mock exchange rate. Use when the user requests currency conversion like USD to EUR.",
            "parameters": {
                "type": "object",
                "properties": {
                    "amount": {
                        "type": "number",
                        "description": "Amount to convert",
                    },
                    "from_currency": {
                        "type": "string",
                        "description": "Source currency code (e.g., USD)",
                    },
                    "to_currency": {
                        "type": "string",
                        "description": "Target currency code (e.g., EUR)",
                    },
                },
                "required": ["amount", "from_currency", "to_currency"],
            },
        },
    },
]


def add_numbers(a: float, b: float):
    return a + b


def multiply_numbers(a: float, b: float):
    return a * b

def subtract_numbers(a: float, b: float):
    return a - b

def calculate_percentage_difference(a: float, b: float):
    if a == 0:
        raise ValueError("First value cannot be zero for percentage difference calculation")
    difference = abs(a - b)
    percentage_diff = (difference / abs(a)) * 100
    return percentage_diff

def calculate_return_on_investment(investment: float, return_amount: float):
    if return_amount < investment:
        raise ValueError("Return amount must be greater than investment")
    roi = ((return_amount - investment) / investment) * 100
    return roi


def get_stock_price(symbol: str):
    # Placeholder implementation, in real case this would call an API
    stock_prices = {
        "AAPL": 182.34,
        "TSLA": 178.21,
        "GOOGL": 141.90,
        "AMZN": 172.55,
        "MSFT": 410.12,
        "META": 485.33,
        "NVDA": 900.21,
    }
    return stock_prices.get(symbol.upper(), "Stock symbol not found")


def convert_currency(amount: float, from_currency: str, to_currency: str):
    # Placeholder implementation, in real case this would call an API
    exchange_rates = {
        ("USD", "EUR"): 0.85,
        ("EUR", "USD"): 1.18,
        ("USD", "JPY"): 110.00,
        ("JPY", "USD"): 0.0091,
    }
    rate = exchange_rates.get((from_currency.upper(), to_currency.upper()))
    if rate is None:
        return "Currency conversion not supported"
    return amount * rate


TOOL_FUNCS = {
    "add_numbers": add_numbers,
    "multiply_numbers": multiply_numbers,
    "calculate_return_on_investment": calculate_return_on_investment,
    "get_stock_price": get_stock_price,
    "convert_currency": convert_currency,
    "subtract_numbers": subtract_numbers,
    "calculate_percentage_difference": calculate_percentage_difference,
}
