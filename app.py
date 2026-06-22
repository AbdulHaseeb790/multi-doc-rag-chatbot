import streamlit as st
from rag_chain_v2 import ask_question
st.title("document Q&A")
st.write("Ask any Question from your uploaded pdfs.")
question=st.text_input("enter your question")
if st.button("ask"):
    if question:
        with st.spinner("searching your documents."):
            answer=ask_question(question)
        st.success('answer')
        st.write(answer)
    else:
        st.warning("please enter the question first")
