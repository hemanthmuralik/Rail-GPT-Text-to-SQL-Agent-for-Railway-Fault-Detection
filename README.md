# Rail-GPT: Text-to-SQL Agent for Railway Fault Detection

This project is a **Generative AI Agent** designed to query railway inspection data using natural language.

### Tech Stack
* **LLM:** Llama-3-70B (via Groq Cloud)
* **Framework:** LangChain (SQLDatabaseChain)
* **Database:** SQLite

### How it Works
1.  User asks: *"How many cracks were detected in Pune?"*
2.  Agent translates English -> SQL.
3.  Agent queries the database and returns the real-time count.

![Demo Output](demo_result.png)
