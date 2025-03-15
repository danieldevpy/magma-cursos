FROM python:3.12.9-slim

RUN apt update && apt install -y \
    default-libmysqlclient-dev \
    build-essential \
    python3-dev \
    pkg-config && \
    rm -rf /var/lib/apt/lists/*  # Limpa cache do apt para reduzir o tamanho do contêiner

# Define o diretório de trabalho diretamente
WORKDIR /app/src

# Copia o código-fonte para dentro do contêiner
COPY src/ . 

# Atualiza o pip e instala as dependências
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Comando para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
