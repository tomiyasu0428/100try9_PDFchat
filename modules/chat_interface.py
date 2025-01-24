from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from config.settings import Settings


def setup_qa_chain(vector_store):
    return RetrievalQA.from_chain_type(
        llm=OpenAI(temperature=Settings.TEMPERATURE),
        chain_type="stuff",
        retriever=vector_store.as_retriever(),
        return_source_documents=True,
    )
