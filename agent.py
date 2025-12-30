import os
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

# 1. SETUP API KEY ---------------------------------------------------------
# Try to load from .env file (Professional Way)
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Fallback: If .env fails, paste key here (The Easy Way)
if not api_key:
    # PASTE YOUR KEY INSIDE THE QUOTES BELOW IF .ENV DOESN'T WORK
    api_key = "gsk_REPLACE_THIS_WITH_YOUR_KEY" 

if not api_key or "gsk_" not in api_key:
    print("❌ ERROR: API Key is missing. Please set it in .env or paste it in the code.")
    exit()

os.environ["GROQ_API_KEY"] = api_key

# 2. CONNECT TO DATABASE ---------------------------------------------------
db = SQLDatabase.from_uri("sqlite:///railway.db")

# 3. INITIALIZE THE BRAIN (Groq Llama-3) -----------------------------------
llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0)

# 4. DEFINE STRICT PROMPT (Prevents Hallucinations) ------------------------
STRICT_PROMPT = PromptTemplate(
    input_variables=["input", "table_info", "dialect"],
    template="""Given an input question, first create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
    
    IMPORTANT RULES:
    1. Only use the table named 'faults'.
    2. Do NOT explain your logic. Just write the SQL.
    3. Do NOT wrap the query in markdown (no ```sql).
    4. Just return the raw SQL query starting with SELECT.

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

# 5. CREATE THE AGENT CHAIN ------------------------------------------------
db_chain = SQLDatabaseChain.from_llm(
    llm, 
    db, 
    prompt=STRICT_PROMPT, 
    verbose=True
)

# 6. DEFINE SECURITY GUARDRAIL (The "Bouncer") -----------------------------
def is_safe_input(user_input):
    """
    Checks the user's question for dangerous keywords before sending to AI.
    """
    # List of words that might modify the database
    dangerous_keywords = ['delete', 'drop', 'truncate', 'insert', 'update', 'alter', 'remove']
    
    clean_input = user_input.lower()
    
    for word in dangerous_keywords:
        # Check if the word exists as a distinct word (not part of another word)
        if f" {word} " in f" {clean_input} ":
            return False, f"Request blocked. The word '{word}' is not allowed."
            
    return True, "Safe"

# 7. MAIN INTERFACE LOOP ---------------------------------------------------
print("\n🚄 --- Rail-GPT (Secure Enterprise Version) is Ready ---")
print("I am connected to your Railway Fault Database.")
print("Try asking: 'How many cracks are pending?'")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    
    # --- SECURITY CHECK ---
    is_safe, message = is_safe_input(user_input)
    if not is_safe:
        print(f"🛡️ SECURITY ALERT: {message}\n")
        continue  # Skip the AI and ask for new input

    try:
        # --- RUN AI ---
        result = db_chain.invoke(user_input)
        print(f"🤖 AI: {result['result']}\n")
    except Exception as e:
        print(f"Error: {e}")
