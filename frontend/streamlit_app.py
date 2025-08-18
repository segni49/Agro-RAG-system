import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
from rag.qa_chain import qa_chain

# ✅ Page config
st.set_page_config(page_title="AgroTreeLink QA", layout="centered")

# ✅ Title
st.title("🌿 Do you Have a question about agriculture ?")

# ✅ Input
query = st.text_input("Ask a question about soil, crops, or farming:")

# ✅ Submit
if query:
    with st.spinner("Thinking..."):
        response = qa_chain.run(query)
    st.success("Answer:")
    st.write(response)