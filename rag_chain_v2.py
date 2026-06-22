from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv(dotenv_path=r'C:\Users\SOHAIL\phase7-llm-apis\.env')
embedding_model=GoogleGenerativeAIEmbeddings(model='gemini-embedding-001')
vector_store=FAISS.load_local('faiss_index_v2',embedding_model,allow_dangerous_deserialization=True)
retriver=vector_store.as_retriever(search_kwargs={"k":3})
llm=ChatGroq(model='llama-3.3-70b-versatile')
prompt=ChatPromptTemplate.from_template("""
 You are a helpful assistant. Answer the question ONLY from the provided context.
If the answer is not in the context, say "I don't have this information in my documents."
Do not use any outside knowledge.
context:{context}
question:{question}

 """)
def ask_question(query):
    docs=retriver.invoke(query)
    context = "\n\n".join([doc.page_content for doc in docs])
    chain=prompt|llm|StrOutputParser()
    return chain.invoke({'context':context,'question':query})
if __name__=='__main__':
    question='what is machine learning?'
    answer=ask_question(question)
    print("answer",answer)


