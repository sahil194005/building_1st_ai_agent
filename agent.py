
from dotenv import load_dotenv
from pydantic import ValidationError
from validator import validate_and_execute
from ollama import chat

load_dotenv()

SYSTEM_PROMPT = """
You are an AI agent that can answer questions or use tools.

If a tool is required, call the appropriate tool.

If the answer is known without tools, respond with:

FINAL_ANSWER: <answer>

If you receive a tool result (Observation), use it to produce the final answer unless another tool is required.
"""

def ask_llm(messages: list, tools: list):
    response = chat(
        model="qwen2.5",
        messages=messages,
        tools=tools,
    )
    return response


def simulate_agent(user_query: str, tools: list, max_steps: int = 7):
    step = 0
    try:

        messages: list = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query},
        ]

        for step in range(max_steps):

            print(f"\n--- Agent Step {step+1} ---")

            response = ask_llm(messages, tools)
            # -------------------------
            # TOOL CALL
            # -------------------------
           
            text = response.message.content
            print("LLM response:", text)
            
            if "FINAL_ANSWER:" in text:
                return text.split("FINAL_ANSWER:")[1].strip()
            
            if  response.message.tool_calls:
                call = response.message.tool_calls[0]
                tool_name = call.function.name
                arguments = dict(call.function.arguments)

                print("Tool selected:", tool_name)
                print("Arguments:", arguments)

                try:
                    result = validate_and_execute(tool_name, arguments)
                except ValidationError as e:
                    result = {"error": "Invalid arguments", "details": e.errors()}
                except Exception as e:
                    result = {"error": str(e)}

                print("Observation:", result)

                # add tool call message
                messages.append(
                    {
                        "role": "model",
                        "content": f"Action: {tool_name}\nAction Input: {arguments}"
                    }
                )

                messages.append(
                    {
                        "role": "user",
                        "content": f"Observation: {result}",
                    }
                )

                continue

        return "Agent stopped: max steps reached."
    except Exception as e:
        return f"Error during agent {step+1} execution: {str(e)}"
