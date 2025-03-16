FROM python:3.12.9-slim

# Instala as dependências do sistema
RUN apt update && apt install -y \
    default-libmysqlclient-dev \
    build-essential \
    python3-dev \
    pkg-config && \
    rm -rf /var/lib/apt/lists/*  # Limpa cache do apt para reduzir o tamanho do contêiner

# Define o diretório de trabalho
WORKDIR /app

# Copia apenas o arquivo de requisitos para o contêiner
COPY src/requirements.txt .

# Atualiza o pip e instala as dependências
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copia o restante do código-fonte para o contêiner
COPY src/ /app/src

# Comando para iniciar o servidor Django
CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]