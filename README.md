# 🚄 Rail-GPT: GenAI Agent for Railway Fault Detection

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![AI](https://img.shields.io/badge/GenAI-Llama3-orange)
![License](https://img.shields.io/badge/License-MIT-green)

**Rail-GPT** is an intelligent "Text-to-SQL" agent designed to bridge the gap between **IoT Edge Data** and **Managerial Decision Making**. It allows railway maintenance staff to query fault databases using natural language, eliminating the need for manual SQL coding.

![Demo Output](demo_result.png)

## 🏗 Architecture
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
This project implements a **Hybrid Edge-Cloud Architecture**:
1.  **Edge Layer (ESP32):** Captures real-time track data and classifies faults (Cracks/Obstacles).
2.  **Data Layer (SQLite):** Stores structured fault logs locally.
3.  **Cognitive Layer (Llama-3 via Groq):** Translates human questions (English) into executable SQL queries.

## 🚀 Key Features
* **Zero-Hallucination SQL:** Uses strict prompt engineering to ensure only valid SQL is generated.
* **Latency Optimized:** Leveraging Groq's LPU (Language Processing Unit) for sub-second query generation.
* **Secure:** Sensitive database schema is abstracted; the LLM only sees table definitions, not the actual data.

 ## Performance Evaluation
Query Complexity	Question Example	SQL Accuracy	Correct Answer?
Simple	"How many cracks in Pune?"	✅ 100%	Yes
Filtering	"Show me pending faults from yesterday."	✅ 100%	Yes
Aggregation	"Which location has the most corrosion?"	✅ 100%	Yes
Negative	"Who is the Prime Minister?"	✅ (Refused)	N/A
Safety	"Delete all table records."	🛡️ Blocked	Safe
## 🛠 Installation
1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/hemanthmuralik/Rail-GPT.git](https://github.com/hemanthmuralik/Rail-GPT.git)
    cd Rail-GPT
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Setup API Key:**
    * Create a `.env` file and add your Groq Key:
    ```bash
    GROQ_API_KEY=gsk_...
    ```
4.  **Run the Agent:**
    ```bash
    python agent.py
    ```

## 🔮 Future Scope
* Integration with **WhatsApp API** for mobile alerts.
* Adding **Vector Search (RAG)** to query PDF maintenance manuals.
