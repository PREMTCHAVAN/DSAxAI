import config

import google.generativeai as genai
from src.core.daily_engine import get_today_problem
from src.core.recommender import get_recommendations


def daily_dsa_agent():
    topic, problem, index, total = get_today_problem()

    # -------- 🌟 PROGRESS SYSTEM --------
    completed = index + 1
    percent = (completed / total) * 100

    if percent <= 20:  
        stars = "★☆☆☆☆"
    elif percent <= 40: 
        stars = "★★☆☆☆"
    elif percent <= 60: 
        stars = "★★★☆☆"
    elif percent <= 80: 
        stars = "★★★★☆"
    else: 
        stars = "★★★★★"

    # -------- GEMINI OUTPUT --------
    prompt = f"""
    You are an AI DSA mentor.

    Problem: {problem}
    Topic: {topic}

    Return strictly ONLY this format:

    🌟 Problem: {problem}
    📌 Topic: {topic}
    🔗 LeetCode: <exact link from leetcode.com>
    🔹 Pattern: <1 line>
    ⚡ Approach: <1 line>
    """


    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content(prompt).text.strip()

    # -------- 📌 GET RECOMMENDATIONS --------
    recommended = get_recommendations(problem)

    final = f"""
================= DSAxAI =================
{response}

🧠 You should practice next:
➡ {recommended[0]}
➡ {recommended[1]}
➡ {recommended[2]}

🌟 Progress: {stars}  ({completed}/{total})
===========================================
"""

    return final
