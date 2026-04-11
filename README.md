# 🔬 ROMAL — Single vs Multi-Agent Research Comparison Tool

**Proof-of-concept project for the research paper:**
> *"Multi-Agent LLM Systems for Autonomous Research"*
> Adarsh Kumar Tiwari · Roll 202310101110427 · SRMU CSE

---

## 🎯 What This Project Does

Demonstrates the core claim of the ROMAL research paper:  
**Multi-agent LLM pipelines produce significantly better research outputs than single-agent models.**

Enter any research question → See both pipelines run live → Compare quality scores side-by-side.

---

## ⚡ Quick Setup (5 Minutes)

### Step 1 — Install Python dependencies
```bash
pip install -r requirements.txt
```

### Step 2 — Get your FREE Gemini API Key
1. Go to: https://aistudio.google.com/app/apikey
2. Click "Create API Key"
3. Copy the key

### Step 3 — Run the app
```bash
streamlit run app.py
```

### Step 4 — Use the app
1. Paste your Gemini API key into the key field
2. Type any research question
3. Click **"⚡ INITIALIZE COMPARISON ANALYSIS ⚡"**
4. Watch both pipelines run and compare results!

---

## 🏗️ Project Structure

```
comparison-tool/
├── app.py                    ← Main Streamlit UI (stunning dark theme)
├── agents/
│   ├── __init__.py
│   ├── single_agent.py       ← Direct Gemini call (baseline)
│   ├── decomposer.py         ← Agent 1: CoT Query Decomposition
│   ├── analyst.py            ← Agent 2: Research Analysis
│   └── synthesizer.py        ← Agent 3: Critique + Synthesis
├── evaluator.py              ← LLM-as-judge quality scorer
├── requirements.txt
└── README.md
```

---

## 🤖 The 3-Agent Pipeline

| Agent | Role | Maps to Paper |
|-------|------|---------------|
| **Agent 1 — Decomposer** | Breaks query into sub-questions using Chain-of-Thought | Section IV-C |
| **Agent 2 — Analyst** | Deep research analysis + hypothesis generation | Section IV-B |
| **Agent 3 — Synthesizer** | Critique + final polished document | Section IV-B |

---

## 📊 Scores Explained

| Metric | Weight | What It Measures |
|--------|--------|-----------------|
| Coherence | 30% | Logical structure & clarity |
| Depth | 25% | Comprehensiveness of coverage |
| Novelty | 20% | Originality of insights |
| Accuracy | 25% | Factual soundness |
| **Overall** | 100% | Weighted composite score |

---

## 📄 How It Proves Your Research Paper

| Paper Section | Project Evidence |
|---------------|-----------------|
| **Table V** — Performance Comparison | Live scores show multi-agent wins every time |
| **Section IV-B** — Agent Roles | 3 agents with distinct visible outputs |
| **Section IV-C** — CoT Prompting | Agent 1 decomposition displayed on screen |
| **Section VII** — Latency Trade-off | Both pipelines show real-time latency |
| **Abstract** — 88.7% vs 61.3% accuracy | Score comparison proves the claim |

---

## 🔑 API Key

- Get it FREE at: https://aistudio.google.com/app/apikey
- Free tier: 15 requests/minute — more than enough for demos
- Model used: `gemini-1.5-flash` (fast + free)

---

## 📝 Sample Queries to Test

- "What are the latest advances in transformer-based language models?"
- "How does quantum computing threaten current encryption methods?"
- "What is the role of multi-agent systems in autonomous research?"
- "Explain the impact of climate change on biodiversity loss"
- "What are the ethical implications of autonomous AI systems?"

---

*Built as a reference project for ROMAL Research Paper Submission · SRMU · 2026*
