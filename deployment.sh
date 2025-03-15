#!/bin/bash

# Mudar para o diretório onde o script está localizado
cd "$(dirname "$0")"

echo "Iniciando deployment..."
echo "Usuário atual: $(whoami)"
git pull origin master
docker compose down
docker compose up -d --build
echo "Deployment concluído!"