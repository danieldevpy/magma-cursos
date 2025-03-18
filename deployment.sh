echo "Iniciando deployment..."

echo "Executando git pull..."

git pull origin master
if [ $? -ne 0 ]; then
    echo "Erro ao executar git pull"
    exit 1
fi

echo "Executando docker compose build"
docker compose build
if [ $? -ne 0 ]; then
    echo "Erro ao executar docker compose build"
    exit 1
fi

echo "Executando docker compose stop..."
docker compose stop django-magma
if [ $? -ne 0 ]; then
    echo "Erro ao executar docker compose stop"
    exit 1
fi

echo "Executando docker compose up..."
docker compose up django-magma -d
if [ $? -ne 0 ]; then
    echo "Erro ao executar docker compose up"
    exit 1
fi

echo "Deployment concluído!"