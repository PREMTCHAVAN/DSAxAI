from dotenv import load_dotenv
import os

load_dotenv()
print("ENV KEY =", os.getenv("GOOGLE_API_KEY"))
