FROM python:3.11-slim

WORKDIR /app
ENV PYTHONPATH=/app

# Dependências de sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instala as bibliotecas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o projeto
COPY . .

# Porta padrão do Streamlit
EXPOSE 8501

# Comando para rodar o app
CMD ["streamlit", "run", "app/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]