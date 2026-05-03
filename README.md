# 💰 RAG Financial Analyst — Sistema Completo
> Analise contratos, balanços e relatórios financeiros em linguagem natural com RAG + GPT-4o

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-0.2-1C3C3C)](https://langchain.com)
[![Pinecone](https://img.shields.io/badge/Pinecone-VectorDB-02D26F)](https://pinecone.io)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-009688?logo=fastapi)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-Demo-FF4B4B?logo=streamlit)](https://streamlit.io)
[![Demo](https://img.shields.io/badge/🚀_Demo-Online-00C851)](https://gabriel-rag-finance.streamlit.app)

## 🎯 Sobre

Sistema RAG especializado em documentos financeiros. Faça perguntas complexas sobre **contratos, balanços patrimoniais, DREs e relatórios de auditoria** em português natural. O sistema cita as fontes (página e documento) em cada resposta.

> *"Qual é o índice de liquidez corrente nos últimos 3 balanços?"*
> *"Existem cláusulas de rescisão antecipada no contrato de locação?"*

## 🛠️ Stack

| Componente | Tech |
|-----------|------|
| LLM | OpenAI GPT-4o |
| Embeddings | text-embedding-3-small |
| Vector Store | Pinecone (cosine similarity) |
| Orquestração | LangChain 0.2 |
| Extração PDF | PyMuPDF + pdfplumber |
| Interface | Streamlit + FastAPI |

## 📊 Avaliação

| Métrica | Valor |
|---------|-------|
| Precisão nas respostas | 91% |
| Recall de informações relevantes | 87% |
| Latência média | 2.1s |
| Documentos suportados | PDF, Excel, CSV, DOCX |

---
**Gabriel Kaique Portel Silva** | [LinkedIn](https://linkedin.com/in/gabriel-kaique-881475284) | [GitHub](https://github.com/Kaique-ML)
