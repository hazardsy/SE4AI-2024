docker exec -it <container name> sh
docker cp <container name>:/app/logs/translations.jsonl .

docker run -p 80:80 -v ./logs:/app/logs translator:latest

kubectl scale --replicas=3 deployment/translator-deployment