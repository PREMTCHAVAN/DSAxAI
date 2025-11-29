import google.generativeai as genai

# paste your API key inside quotes
genai.configure(api_key="AIzaSyC79Rnm1DnGZcrP23ZHPi6Oh3ehkcd56fU")

# list available models
models = genai.list_models()

print("\n🔍 Models available for your key:\n")
for m in models:
    print("➡", m.name)
