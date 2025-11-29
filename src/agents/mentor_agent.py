import config  
import google.generativeai as genai


def mentor_agent(topic, problem):

    prompt = f"""
    You are an AI DSA mentor.

    Problem: {problem}
    Topic: {topic}

    Return strictly ONLY:

    🌟 Problem: {problem}
    📌 Topic: {topic}
    🔗 LeetCode: <exact link>
    🔹 Pattern: <1 line>
    ⚡ Approach: <1 line>
    """

    model = genai.GenerativeModel("models/gemini-2.5-flash")
    result = model.generate_content(prompt).text.strip()

    return result
