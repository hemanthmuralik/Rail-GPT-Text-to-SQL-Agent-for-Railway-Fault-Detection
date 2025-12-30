import streamlit as st
import os
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Page Config
st.set_page_config(page_title="Rail-GPT Interface", page_icon="🚄")
st.title("🚄 Rail-GPT: Railway Fault Detective")

# Sidebar
st.sidebar.header("System Status")
st.sidebar.success("Database: Connected (railway.db)")
st.sidebar.info("Model: Llama-3-70B (Groq)")

# Setup (Same logic as agent.py)
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("❌ API Key missing! Check .env file.")
    st.stop()

os.environ["GROQ_API_KEY"] = api_key
db = SQLDatabase.from_uri("sqlite:///railway.db")
llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0)
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

# Chat Interface
query = st.text_input("Ask a question about track faults:", placeholder="e.g., How many cracks were detected in Pune?")

if query:
    # Security Check
    dangerous_keywords = ['delete', 'drop', 'truncate', 'insert', 'update']
    if any(word in query.lower() for word in dangerous_keywords):
        st.error("🛡️ SECURITY ALERT: Dangerous command blocked.")
    else:
        with st.spinner("Analyzing Database..."):
            try:
                response = db_chain.run(query)
                st.success("Analysis Complete")
                st.markdown(f"**🤖 AI Answer:** {response}")
            except Exception as e:
                st.error(f"Error: {e}")

# Footer
st.markdown("---")
st.caption("Powered by LangChain & Groq | Hybrid Edge-Cloud Architecture")
