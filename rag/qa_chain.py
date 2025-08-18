import os
import json
import faiss
from dotenv import load_dotenv
load_dotenv()

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from sentence_transformers import SentenceTransformer
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(BASE_DIR, "..", "embeddings", "agro_index.faiss")
CHUNKS_PATH = os.path.join(BASE_DIR, "..", "embeddings", "agro_chunks.json")
index = faiss.read_index(INDEX_PATH)

with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
    chunks = json.load(f)
    
documents = [Document(page_content=chunk) for chunk in chunks]    
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(documents, embedding_model)

openai_api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    temperature=0.3,
    model_name="gpt-3.5-turbo",
 openai_api_key=os.getenv("OPENAI_API_KEY")
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
    chain_type="stuff"
)

