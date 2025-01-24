from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from config.settings import Settings


def process_pdf(file):
    """PDF処理パイプライン"""
    pdf = PdfReader(file)
    text_chunks = []
    
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        if text.strip():  # 空のページをスキップ
            splitter = CharacterTextSplitter(
                separator="\n",
                chunk_size=Settings.CHUNK_SIZE,
                chunk_overlap=Settings.CHUNK_OVERLAP,
                length_function=len,
            )
            chunks = splitter.split_text(text)
            text_chunks.extend([(chunk, {"page": i}) for chunk in chunks])
    
    return text_chunks
