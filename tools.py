from google import genai


tools = [
    genai.types.Tool(
        function_declarations=[
            genai.types.FunctionDeclaration(
                name="calculate_return_on_investment",
                description="Calculate ROI percentage from investment and return amount. Use when user asks about profit percentage or investment performance.",
                parameters={
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
            ),
            genai.types.FunctionDeclaration(
                name="add_numbers",
                description="Add two numbers",
                parameters={
                    "type": "object",
                    "properties": {
                        "a": {"type": "number"},
                        "b": {"type": "number"},
                    },
                    "required": ["a", "b"],
                },
            ),
            genai.types.FunctionDeclaration(
                name="multiply_numbers",
                description="Multiply two numbers",
                parameters={
                    "type": "object",
                    "properties": {
                        "a": {"type": "number"},
                        "b": {"type": "number"},
                    },
                    "required": ["a", "b"],
                },
            ),
            genai.types.FunctionDeclaration(
                name="get_stock_price",
                description="Get the current price of a stock",
                parameters={
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string"},
                    },
                    "required": ["symbol"],
                },
            ),
            genai.types.FunctionDeclaration(
                name="convert_currency",
                description="Convert currency from one type to another",
                parameters={
                    "type": "object",
                    "properties": {
                        "amount": {"type": "number"},
                        "from_currency": {"type": "string"},
                        "to_currency": {"type": "string"},
                    },
                    "required": ["amount", "from_currency", "to_currency"],
                },
            ),
        ],
    ),
]


def add_numbers(a: float, b: float):
    return a + b


def multiply_numbers(a: float, b: float):
    return a * b


def calculate_return_on_investment(investment: float, return_amount: float):
    if return_amount < investment:
        raise ValueError("Return amount must be greater than investment")
    roi = ((return_amount - investment) / investment) * 100
    return roi


def get_stock_price(symbol: str):
    # Placeholder implementation, in real case this would call an API
    stock_prices = {
        "AAPL": 150.00,
        "GOOGL": 2800.00,
        "AMZN": 3400.00,
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
}
