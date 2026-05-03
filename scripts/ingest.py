"""Indexa documentos financeiros no Pinecone."""
import argparse
import os
from pathlib import Path
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from app.ingestion.loader import load_pdf, load_excel
from app.ingestion.chunker import chunk_documents


def ingest(docs_path: str, namespace: str = "default"):
    all_raw = []
    for f in Path(docs_path).glob("*"):
        if f.suffix.lower() == ".pdf":
            all_raw.extend(load_pdf(str(f)))
        elif f.suffix.lower() in (".xlsx", ".xls"):
            all_raw.extend(load_excel(str(f)))

    chunks = chunk_documents(all_raw)
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    PineconeVectorStore.from_documents(
        chunks, embeddings,
        index_name=os.getenv("PINECONE_INDEX"),
        namespace=namespace,
    )
    print(f"✅ {len(chunks)} chunks indexados de {len(all_raw)} páginas/abas")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--docs_path", required=True)
    parser.add_argument("--namespace", default="default")
    args = parser.parse_args()
    ingest(args.docs_path, args.namespace)
