from agent import ask_llm
from tools import tools

def run_test(query: str, expected_tool: str = None):
    print("\n---\nQuery:", query)
    res = ask_llm(query, tools)
    print("Result object:", res)
    if isinstance(res, dict) and expected_tool:
        picked = res.get("tool")
        verdict = "✅" if picked == expected_tool else "❌"
        print(f"Expected tool: {expected_tool}, picked: {picked} {verdict}")
    return res


def main():
    # example questions that should route to specific tools
    test_cases = [
        # ("If I invest 5000 and get 8000 what ROI?", "calculate_return_on_investment"),
        # (
        #     "What is the profit percentage if I put in 1000 and get back 1200?",
        #     "calculate_return_on_investment",
        # ),
        # ("Multiply 8 by 12", "multiply_numbers"),
        # ("Add 15 and 27 together", "add_numbers"),
        # ("What is TSLA stock price?", "get_stock_price"),
        # ("Convert 100 USD to EUR", "convert_currency"),
        ("Compare TSLA and AAPL stock price", "get_stock_price"),
    ]

    for query, expected in test_cases:
        run_test(query, expected)


if __name__ == "__main__":
    main()
