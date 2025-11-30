# DSAxAI — Multi-Agent System for LeetCode 
### Capstone Submission — Google AI Agents Intensive 2025
![capstoneProject](https://github.com/PREMTCHAVAN/DSAxAI/blob/main/capstoneProject_img.png)


---

## 1. Overview

DSAxAI is a multi-agent system built to streamline Data Structures & Algorithms (DSA) preparation for technical interviews.
Instead of selecting problems manually, searching approaches online, and tracking progress in spreadsheets — this agent automates the entire cycle:

**Selects → Explains → Recommends → Tracks**

The system functions as a personal automated LeetCode mentor.

---

## 2. Problem Statement

### DSA learning breakdown today:

| Challenge | Result |
|----------|--------|
| No clear problem progression | Learners jump randomly |
| Approach research takes long | Learning speed slows |
| Progress tracking is manual | Motivation drops |
| No reinforcement pattern | Concept retention weak |

**The issue is not problem difficulty — it is lack of structure.**

---

## 3. Proposed Solution

The system uses **3 sequential agents** to automate the complete study loop:

| Agent | Function |
|-------|----------|
| Planner Agent | Selects the next problem intelligently |
| Mentor Agent | Generates structured explanation + link + pattern |
| Recommender Agent | Suggests related follow-ups for reinforcement |

The user only executes:

```bash
python main.py
```

and learning continues without decision fatigue.

---

<h2>4. Project Structure</h2>

<pre>
DSAxAI
├── src/
│   ├── agents/
│   │   ├── planner_agent.py
│   │   ├── mentor_agent.py
│   │   └── recommender_agent.py
│
├── data/
│   ├── dsa_list.txt
│   ├── history.json
│   ├── problems_meta.json
│   └── progress.json
│
├── main.py
├── config.py
└── requirements.txt
</pre>



---

## 5. Agent Responsibilities

### Planner Agent  
- Reads from `dsa_list.txt`  
- Tracks solved index using `progress.json`  
- Ensures coverage without repetition  

### Mentor Agent  
Produces structured response:

- Problem  
- Topic  
- LeetCode Source  
- Pattern Used  
- Optimized Approach Summary  

Designed for interview-grade understanding in one pass.

### Recommender Agent  
Reads `problems_meta.json` to recommend:

- Similar patterns  
- FAANG company frequency  
- Optimal progression paths  

---

## 6. Data Layer Specification

| File | Contents |
|------|----------|
| dsa_list.txt | Full curated DSA roadmap |
| history.json | Topic-wise count (for expansion) |
| progress.json | Current index in learning pipeline |
| problems_meta.json | Pattern + company mapping JSON |

The system supports unlimited dataset expansion without code rewrites.

---

## 7. Workflow

![workflow](https://github.com/PREMTCHAVAN/DSAxAI/blob/main/workflow.png)

---

## 8. Installation & Run

```bash
git clone https://github.com/PREMTCHAVAN/DSAxAI.git
cd DSAxAI

python -m venv env
env\Scripts\activate         # On Windows
# source env/bin/activate      # For macOS/Linux

pip install -r requirements.txt
```

Create `.env` file inside root directory:

```
GOOGLE_API_KEY=your_key_here
```

Run system:

```bash
python main.py
```

**Output includes:**

- Problem breakdown  
- Approach + pattern  
- Next 3 recommended problems  
- Progress indicator  

---

## 9. Outcome & Value

| Traditional Prep | With DSAxAI |
|------------------|-------------|
| Search problems daily | Auto-assigned problems |
| Google approach blogs | Crisp structured explanation |
| No roadmap continuity | Pattern-based reinforcement |
| Motivation inconsistent | Visible progression counter |

**Estimated time saved → 2–4 hours/day**  
**Knowledge reinforcement → continuous + organized**
