# Exemplo: /home/daniel/apps/meu-projeto/deployment.sh
#!/bin/bash
echo "Iniciando deployment..."
git pull origin master
docker-compose down
docker-compose up -d --build
echo "Deployment concluído!"