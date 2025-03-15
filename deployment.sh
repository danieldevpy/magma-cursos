echo "Iniciando deployment..."
echo "Diretório atual: $(pwd)"
git config --global --add safe.directory "$(pwd)"
echo "Executando git pull..."
git pull origin master
if [ $? -ne 0 ]; then
    echo "Erro ao executar git pull"
    exit 1
fi
echo "Executando docker compose down..."
docker compose down
if [ $? -ne 0 ]; then
    echo "Erro ao executar docker compose down"
    exit 1
fi
echo "Executando docker compose up..."
docker compose up -d --build
if [ $? -ne 0 ]; then
    echo "Erro ao executar docker compose up"
    exit 1
fi
echo "Deployment concluído!"