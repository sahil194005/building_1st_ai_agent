import os

from google import genai
from dotenv import load_dotenv
from pydantic import ValidationError
from tool_executor import execute_tool
from tools import TOOL_FUNCS

load_dotenv()
client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))


def ask_llm(prompt, tools=[]):
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
        config=genai.types.GenerateContentConfig(temperature=0, tools=tools),
    )
    candidate = response.candidates[0]
    content = candidate.content.parts[0]

    if content.function_call:
        tool_name = content.function_call.name
        arguments = dict(content.function_call.args)
        try:
            result = execute_tool(tool_name, arguments)
        except ValidationError as e:
            result = {
                "error": "Invalid tool arguments",
                "details": e.errors()
            }
        print(f"Executing tool: {tool_name}")
        print("Arguments:", arguments)
        func = TOOL_FUNCS.get(tool_name)
        if func is None:
            raise ValueError(f"No Python function registered for tool '{tool_name}'")
        result = func(**arguments)
        print("Function result:", result)
        return result

    return content.text
