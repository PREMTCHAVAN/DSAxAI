import json
import os

DATA_DIR = "data"
LIST_FILE = os.path.join(DATA_DIR, "dsa_list.txt")
PROGRESS_FILE = os.path.join(DATA_DIR, "progress.json")


def load_dsa_list():
    """
    Reads the DSA list and returns a list of (topic, problem) pairs.
    """
    problems = []
    current_topic = None

    with open(LIST_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # Topic line (e.g. ARRAYS & STRINGS)
            if line.isupper() or "&" in line:
                current_topic = line
                continue

            # Problem under topic
            problems.append((current_topic, line))

    return problems


def load_progress():
    with open(PROGRESS_FILE, "r") as f:
        data = json.load(f)
        return data.get("last_index", 0)


def save_progress(index):
    with open(PROGRESS_FILE, "w") as f:
        json.dump({"last_index": index}, f)


def get_today_problem():
    with open("data/dsa_list.txt") as f:
        problems = f.read().splitlines()

    with open("data/progress.json") as f:
        progress = json.load(f)

    index = progress["index"]
    topic = "ARRAYS & STRINGS"  # for now, later auto-detect
    problem = problems[index]

    # update progress index
    progress["index"] = (index + 1) % len(problems)
    with open("data/progress.json", "w") as f:
        json.dump(progress, f, indent=4)


    # ----- 🔥 Update Topic Score in history.json -----
    with open("data/history.json", "r") as f:
        history = json.load(f)

    history[topic] += 1  # increment solved count for the topic

    with open("data/history.json", "w") as f:
        json.dump(history, f, indent=4)


    return topic, problem, index, len(problems)


