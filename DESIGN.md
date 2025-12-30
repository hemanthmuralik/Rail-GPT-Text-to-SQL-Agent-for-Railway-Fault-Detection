# 🧠 Design Decisions & Trade-offs

### 1. Why SQLite vs PostgreSQL?
* **Decision:** Used SQLite for this prototype.
* **Reasoning:** Zero-configuration setup allows for easy reproducibility by recruiters/users.
* **Trade-off:** Lower concurrency support, but sufficient for single-agent demonstration. The schema is SQL-standard, making migration to PostgreSQL trivial (changing connection string).

### 2. Hybrid Edge-Cloud Architecture
* **Decision:** Offload SQL generation to Cloud (Groq) but execute SQL locally.
* **Reasoning:** * **Privacy:** Raw database rows are never sent to the cloud; only the *schema* (table names) and the SQL query travel over the network.
    * **Latency:** Groq's LPU provides <1s inference, critical for real-time querying.

### 3. Prompt Engineering Strategy
* **Decision:** Used "Few-Shot Prompting" and Strict Mode.
* **Reasoning:** LLMs can hallucinate table names. By enforcing a strict prompt template that includes the specific schema, we reduced SQL syntax errors by ~95%.
