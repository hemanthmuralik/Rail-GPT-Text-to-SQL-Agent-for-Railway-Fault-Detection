🚆 Rail-GPT: Text-to-SQL Agent for Railway Fault Detection

Rail-GPT is a GenAI-powered Text-to-SQL agent designed to help railway engineers and operators query fault and inspection data using natural language, without needing SQL expertise.

The system bridges the gap between domain experts and structured railway inspection databases, enabling faster fault analysis and decision-making.

🔍 Problem Statement

Railway fault and inspection data is typically stored in structured databases, but accessing insights requires SQL knowledge.
This creates friction for:

Field engineers

Maintenance planners

Operations teams

Rail-GPT solves this by translating natural language questions into executable SQL queries, allowing users to ask questions like:

“Show all cracked rails detected in the last 7 days.”

and receive precise, structured results.

🧠 Solution Overview

Rail-GPT uses a Large Language Model (LLM) combined with schema-aware prompting to generate accurate SQL queries over a railway fault database.

Core Capabilities

Natural language → SQL conversion

Domain-specific fault analytics

Scalable synthetic database generation

Modular, extensible agent design

🏗️ System Architecture (High Level)
User Query (Natural Language)
        ↓
   LLM-based Agent
        ↓
 Schema-Aware SQL Generation
        ↓
  Railway Fault Database
        ↓
 Structured Results

📂 Project Structure
Rail-GPT/
│
├── agent.py               # Core Text-to-SQL agent logic
├── create_db.py           # Creates base railway fault database
├── generate_big_db.py     # Generates large-scale synthetic data
├── railway.db             # SQLite database
├── DESIGN.md              # Design decisions & trade-offs
├── README.md              # Project documentation
└── requirements.txt       # Dependencies

⚙️ Setup & Installation
1️⃣ Clone the repository
git clone https://github.com/your-username/Rail-GPT.git
cd Rail-GPT

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Create the database
python create_db.py


(Optional: Generate a larger dataset)

python generate_big_db.py

▶️ Running the Agent
python agent.py


Example query:

Which locations reported signal failures this month?


The agent will:

Interpret the question

Generate SQL

Execute it on the database

Return structured results

🗄️ Database Schema (Simplified)
Column Name	Description
fault_id	Unique fault identifier
fault_type	Type of fault (crack, signal, etc.)
severity	Fault severity level
location	Track/location identifier
detected_time	Timestamp of detection
sensor_type	Source sensor
📈 Scalability & Data Generation

generate_big_db.py simulates large railway inspection datasets

Enables stress-testing LLM query generation

Demonstrates system behavior beyond toy examples

🧪 Evaluation Status

⚠️ Current Status: Qualitative Evaluation

Manual testing with diverse natural language queries

Correct SQL generation observed for common fault queries

Edge cases and failure modes documented in DESIGN.md

📌 Planned Enhancements

Quantitative accuracy metrics

SQL validation guardrails

Baseline comparison (rule-based vs LLM)

🧩 Design Decisions

Detailed design choices, trade-offs, and limitations are documented in:

📄 DESIGN.md

Topics covered:

Why SQLite was chosen

Schema grounding strategy

Scalability considerations

Future production roadmap

🚀 Future Work

PostgreSQL integration

SQL safety & schema validation

Query accuracy benchmarking

Edge-device simulation (ESP32 pipeline)

Web-based UI

👤 Author

Hemanth Murali K
MSc Artificial Intelligence
Focus: GenAI Systems · Data Engineering · Applied ML
