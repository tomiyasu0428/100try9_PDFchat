from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from config.settings import Settings
import os


def create_vector_store(texts):
    embeddings = OpenAIEmbeddings(openai_api_key=Settings.OPENAI_API_KEY)
    texts, metadatas = zip(*texts)
    return FAISS.from_texts(list(texts), embeddings, metadatas=list(metadatas))
