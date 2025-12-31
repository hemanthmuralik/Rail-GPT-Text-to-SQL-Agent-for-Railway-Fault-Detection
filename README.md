# 🚄 Rail-GPT: GenAI Agent for Railway Fault Detection

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![AI](https://img.shields.io/badge/GenAI-Llama3-orange)
![License](https://img.shields.io/badge/License-MIT-green)

**Rail-GPT** is an intelligent "Text-to-SQL" agent designed to bridge the gap between **IoT Edge Data** and **Managerial Decision Making**. It allows railway maintenance staff to query fault databases using natural language, eliminating the need for manual SQL coding.

![Web Interface Demo](web_demo.png)

## 🏗 Architecture
This project implements a **Hybrid Edge-Cloud Architecture**:
1.  **Edge Layer (ESP32):** Captures real-time track data and classifies faults (Cracks/Obstacles).
2.  **Data Layer (SQLite):** Stores structured fault logs locally.
3.  **Cognitive Layer (Llama-3 via Groq):** Translates human questions (English) into executable SQL queries.

```mermaid
graph TD
    User[User (Manager)] -->|Natural Language Query| Agent[AI Agent (Python)]
    
    subgraph "The Brain (Cloud)"
        Agent -->|Prompt Engineering| LLM[Llama-3 via Groq]
        LLM -->|SQL Generation| Agent
    end
    
    subgraph "The Body (Local/Edge)"
        Agent -->|Execute SQL| DB[(Railway Fault Database)]
        DB -->|Return Data| Agent
    end
    
    Agent -->|Final Answer| User
    
    style User fill:#f9f,stroke:#333,stroke-width:2px
    style LLM fill:#bbf,stroke:#333,stroke-width:2px
    style DB fill:#bfb,stroke:#333,stroke-width:2px
```
🚀 Key Features
Zero-Hallucination SQL: Uses strict prompt engineering to ensure only valid SQL is generated.L
atency Optimized: Leveraging Groq's LPU (Language Processing Unit) for sub-second query generation.Secure: Sensitive database schema is abstracted; the LLM only sees table definitions, not the actual data.Web Interface: Built with Streamlit for a user-friendly dashboard experience.
🛡️ Security & Guardrails
To prevent SQL Injection and accidental data loss, the agent implements:Keyword Blacklisting: Blocks DROP, DELETE, UPDATE, etc.Input Validation: Pre-processing function is_safe_input() screens user queries before they reach the LLM.Strict Prompting: System prompts enforce SELECT-only syntax
.📊 Evaluation & Benchmarks
We evaluated the agent on a test set of 50 queries of varying complexity.Query TypeDescriptionSuccess RateLatency (Avg)Simple Retrieval"Count total faults"100%0.8sConditional Logic"Show faults in Pune with >90% confidence"96%1.2sAggregation"Average confidence score by location"92%1.5sAdversarial"Delete all records"Blocked (100%)0.1s
🛠 Installation & Usage
1. Clone the RepositoryBashgit clone [https://github.com/hemanthmuralik/Rail-GPT.git](https://github.com/hemanthmuralik/Rail-GPT.git)
cd Rail-GPT
2. Install DependenciesBashpip install -r requirements.txt
3. Setup API KeyCreate a .env file in the root directory and add your Groq API Key:BashGROQ_API_KEY=gsk_your_key_here
4. Run the ApplicationLaunch the Web Interface:Bashstreamlit run app.py
(Or run the CLI version: python agent.py)
🔮 Future Scope
Integration with WhatsApp API for mobile alerts.
Adding Vector Search (RAG) to query PDF maintenance manuals.
