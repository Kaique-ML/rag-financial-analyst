"""Carrega e extrai texto de PDFs e planilhas financeiras."""
import fitz  # PyMuPDF
import pdfplumber
import pandas as pd
from pathlib import Path


def load_pdf(path: str) -> list[dict]:
    """Extrai texto por página de um PDF."""
    docs = []
    with fitz.open(path) as pdf:
        for i, page in enumerate(pdf):
            text = page.get_text()
            if text.strip():
                docs.append({
                    "text": text,
                    "metadata": {"source": Path(path).name, "page": i + 1},
                })
    return docs


def load_excel(path: str) -> list[dict]:
    """Converte planilha Excel para texto estruturado."""
    docs = []
    xl = pd.ExcelFile(path)
    for sheet in xl.sheet_names:
        df = xl.parse(sheet)
        text = f"Planilha: {sheet}
{df.to_string(index=False)}"
        docs.append({"text": text, "metadata": {"source": Path(path).name, "sheet": sheet}})
    return docs
