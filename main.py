from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

from src.agents.planner_agent import planner_agent
from src.agents.mentor_agent import mentor_agent
from src.core.recommender import get_recommendations



def run_dsa_agent():

    # ========== AGENT 1 → QUESTION PLANNER ==========
    plan = planner_agent()
    topic = plan["topic"]
    problem = plan["problem"]
    index = plan["index"]
    total = plan["total"]

    # ========== AGENT 2 → AI MENTOR ==========
    mentor_response = mentor_agent(topic, problem)

    # ========== AGENT 3 → RECOMMENDER ==========
    recommended = get_recommendations(problem)

    # --------- PROGRESS SYSTEM ---------
    completed = index + 1
    percent = (completed / total) * 100

    stars = ["★☆☆☆☆","★★☆☆☆","★★★☆☆","★★★★☆","★★★★★"][
        min(4, int(percent // 20))
    ]

    # --------- FINAL OUTPUT ---------
    print(f"""
================= 🔥 DSAxAI — Multi-Agent System =================

{mentor_response}


🧠 Recommended Next Problems:
""" + "\n".join([f"➡ {q}" for q in recommended[:3]]) + f"""

📊 Progress — {stars}  ({completed}/{total})
=================================================================
""")


if __name__ == "__main__":
    run_dsa_agent()
