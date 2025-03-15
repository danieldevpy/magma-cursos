# Exemplo: /home/daniel/apps/meu-projeto/deployment.sh
#!/bin/bash
echo "Iniciando deployment..."
git pull -f
docker-compose down
docker-compose up -d --build
echo "Deployment concluído!"