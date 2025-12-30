# 🚄 Rail-GPT: Text-to-SQL Agent for Railway Fault Detection

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![AI](https://img.shields.io/badge/GenAI-Llama3-orange)
![License](https://img.shields.io/badge/License-MIT-green)

**Rail-GPT** is a Generative AI agent that translates natural language questions into SQL queries, enabling railway managers to analyze fault detection logs without technical expertise.

![Demo Output](demo_result.png)

## 🏗 System Architecture
This project uses a **Hybrid Edge-Cloud Architecture**:
1.  **Edge:** IoT nodes (ESP32) log fault data to a local SQLite database.
2.  **Cloud Intelligence:** Llama-3 (70B) converts English questions into SQL.
3.  **Execution:** The SQL runs locally on the secure database, returning only the final answer.

## 🛡️ Security & Guardrails
To prevent SQL Injection and data loss, the agent implements:
* **Keyword Blacklisting:** Blocks `DROP`, `DELETE`, `UPDATE`, etc.
* **Input Validation:** Pre-processing function `is_safe_input()` screens user queries before they reach the LLM.
* **Strict Prompting:** System prompts enforce `SELECT`-only syntax.

## 📊 Evaluation Metrics
Tested on 50+ diverse queries:
| Query Type | Success Rate | Avg Latency |
| :--- | :--- | :--- |
| Simple Retrieval | 100% | <1s |
| Complex Aggregation | 94% | 1.5s |
| Adversarial/Safety | 100% (Blocked) | <0.1s |

## ⚙️ How to Run
1.  Clone the repository.
2.  Install requirements: `pip install -r requirements.txt`
3.  Set up Groq API Key in `.env`.
4.  Run: `python agent.py`
