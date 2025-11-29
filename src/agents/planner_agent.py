from src.core.daily_engine import get_today_problem

def planner_agent():
    topic, problem, index, total = get_today_problem()

    return {
        "topic": topic,
        "problem": problem,
        "index": index,
        "total": total
    }
