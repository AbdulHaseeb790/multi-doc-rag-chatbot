from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
load_dotenv(dotenv_path=r'C:\Users\SOHAIL\phase7-llm-apis\.env')
loader=DirectoryLoader(
    r"C:\Users\SOHAIL\phase7-llm-apis\lang_chain\Rag\docs",
    glob="**/*.pdf",
    loader_cls=PyPDFLoader


)
docs=loader.load()
print("total pages loaded",len(docs))
splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
chunks=splitter.split_documents(docs)
print("total chunks",len(chunks))

embeding_model=GoogleGenerativeAIEmbeddings(model='gemini-embedding-001')
vector_store=FAISS.from_documents(chunks,embeding_model)
print("vectors stores createddddd guysss")
vector_store.save_local("faiss_index_v2")
print('saved to disk')