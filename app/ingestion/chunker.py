"""Chunking semântico de documentos financeiros."""
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document


def chunk_documents(raw_docs: list[dict], chunk_size: int = 1000, overlap: int = 150) -> list[Document]:
    """Divide documentos em chunks para indexação."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,
        separators=["

", "
", ".", " "],
    )
    documents = [Document(page_content=d["text"], metadata=d["metadata"]) for d in raw_docs]
    return splitter.split_documents(documents)
