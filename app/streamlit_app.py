import os
import sys
import streamlit as st

# Adiciona o diretório raiz ao path do sistema para resolver os imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Agora o import funciona sem o prefixo "app."
from app.rag.chain import create_rag_chain

st.set_page_config(page_title="RAG Financial Analyst", layout="wide")
st.title("💰 RAG Financial Analyst")
st.caption("Analise documentos financeiros em linguagem natural")

with st.sidebar:
    namespace = st.text_input("Namespace (empresa)", value="default")
    st.markdown("**Exemplos de perguntas:**")
    st.markdown("- Qual o índice de liquidez corrente?")
    st.markdown("- Compare a margem EBITDA dos últimos 4 trimestres")
    st.markdown("- Existem cláusulas de rescisão antecipada?")

if "chain" not in st.session_state:
    st.session_state.chain = create_rag_chain(namespace)

query = st.chat_input("Faça uma pergunta sobre os documentos financeiros...")
if query:
    with st.spinner("Analisando documentos..."):
        result = st.session_state.chain.invoke({"query": query})
    st.markdown(result["result"])
    with st.expander("📚 Fontes utilizadas"):
        for doc in result.get("source_documents", []):
            st.caption(f"📄 {doc.metadata}")
