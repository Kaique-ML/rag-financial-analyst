"""LangChain RetrievalQA especializado em documentos financeiros."""
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.prompts import PromptTemplate
import os

FINANCIAL_PROMPT = PromptTemplate(
    template="""Você é um analista financeiro especializado. Use apenas o contexto abaixo para responder.
Sempre cite a fonte (documento e página) ao final da resposta.

Contexto:
{context}

Pergunta: {question}

Resposta (em português, citar fonte):""",
    input_variables=["context", "question"],
)


def create_rag_chain(namespace: str = "default") -> RetrievalQA:
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vectorstore = PineconeVectorStore(
        index_name=os.getenv("PINECONE_INDEX", "financial-docs"),
        embedding=embeddings,
        namespace=namespace,
    )
    return RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model="gpt-4o", temperature=0),
        retriever=vectorstore.as_retriever(search_kwargs={"k": 6}),
        chain_type_kwargs={"prompt": FINANCIAL_PROMPT},
        return_source_documents=True,
    )
