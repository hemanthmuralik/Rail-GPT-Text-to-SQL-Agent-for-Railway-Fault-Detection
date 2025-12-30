import os
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_groq import ChatGroq
# UPDATED IMPORT: This is the modern path that won't crash
from langchain_core.prompts import PromptTemplate

# ==========================================
# 🔑 PASTE YOUR GROQ API KEY HERE
# ==========================================
api_key = "" # <--- PASTE YOUR KEY HERE

if " " not in api_key:
    print("❌ ERROR: You forgot to paste the key!")
    exit()

os.environ["GROQ_API_KEY"] = api_key

# 1. Connect to database
db = SQLDatabase.from_uri("sqlite:///railway.db")

# 2. Initialize the Brain
llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0)

# 3. Create the "Strict" Prompt
STRICT_PROMPT = PromptTemplate(
    input_variables=["input", "table_info", "dialect"],
    template="""Given an input question, first create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
    
    IMPORTANT: 
    - Only use the table named 'faults'. 
    - Do NOT explain your logic. 
    - Do NOT wrap the query in markdown. 
    - just return the raw SQL query.

    Use the following format:

    Question: "Question here"
    SQLQuery: "SQL Query to run"
    SQLResult: "Result of the SQLQuery"
    Answer: "Final answer here"

    Only use the following tables:
    {table_info}

    Question: {input}
    """
)

# 4. Create the Chain
db_chain = SQLDatabaseChain.from_llm(
    llm, 
    db, 
    prompt=STRICT_PROMPT, 
    verbose=True
)

# 5. Run the Interface
print("\n🚄 --- Rail-GPT (Strict Version) is Ready ---")
print("I am connected to your Railway Fault Database.")
print("Ask me anything! (Type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    
    try:
        # We use .invoke() safely
        result = db_chain.invoke(user_input)
        print(f"🤖 AI: {result['result']}\n")
    except Exception as e:
        print(f"Error: {e}")
