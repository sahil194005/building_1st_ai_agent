from llm import ask_llm
from tools import tools
prompt = "User query: If I invest 5000 and get 8000 what ROI?"

response = ask_llm(prompt, tools)
print(response)
