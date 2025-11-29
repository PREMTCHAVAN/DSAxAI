from dotenv import load_dotenv
import google.generativeai as genai

# paste your API key inside quotes
genai.configure(api_key="GOOGLE_API_KEY")

# list available models
models = genai.list_models()

print("\n🔍 Models available for your key:\n")
for m in models:
    print("➡", m.name)
