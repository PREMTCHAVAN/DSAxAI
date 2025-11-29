import json
import random


def get_recommendations(current_problem):
    with open("data/problems_meta.json") as f:
        data = json.load(f)

    # search inside every topic
    for topic, problems in data.items():
        for p in problems:
            if p["name"].lower() == current_problem.lower():
                pattern = p["pattern"]
                company = set(p["company"])

                # find similar questions
                similar = []
                for q in problems:
                    if q["name"] != current_problem:
                        score = 0

                        # same pattern → +2 points
                        if q["pattern"] == pattern:
                            score += 2

                        # same company → +1 each
                        score += len(company.intersection(q["company"]))

                        if score > 0:
                            similar.append((score, q["name"]))

                # sort by best match
                similar.sort(reverse=True)

                # return top 3 matches
                return [name for _, name in similar[:3]]

    return ["No similar problems found"]
