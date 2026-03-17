from agent import ask_llm, simulate_agent
from tools import tools

plan_prompt = """You are an AI planning agent.
Break the user request into a sequence of steps using available tools.
Only include steps that require tool usage."""

def run_test(query: str):
    print("\n---\nQuery:", query)
    
    generate_plan(plan_prompt + "\n\nUser request: " + query)
    res = simulate_agent(query, tools)
    print("Result object:", res)
    return res

def generate_plan(query: str):
    print("\n---\nGenerating plan for query:")
    messages: list = [
        {"role": "system", "content": plan_prompt},
        {"role": "user", "content": query},
    ]
    res = ask_llm(messages, tools)
    for tool_call in res.message.tool_calls:
        print("Tool call:", tool_call.function.name)
        print("Arguments:", tool_call.function.arguments)
        print("\n\n")
    # print("Plan:", res.message.tool_calls)
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
        ("Compare Tesla and Apple stock prices and calculate the percentage difference."),
    ]

    for query in test_cases:
        run_test(query)


if __name__ == "__main__":
    main()
