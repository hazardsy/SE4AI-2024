# SE4AI-2024

## Lien du TP
[Ici](https://tinyurl.com/se4ai-2024)

## Liens d'installation
- [Installing Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/) et [Post-installation steps for Ubuntu](https://docs.docker.com/engine/install/linux-postinstall/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/) et [kubectl](https://kubernetes.io/docs/tasks/tools/)

## Commandes utiles
### FastAPI
#### Démarrer une API en mode développement
```sh
fastapi dev --port <PORT> <FICHIER.py>
fastapi dev --port 3000 main.py
```

Pour lancer en mode "production", remplacer `dev` par `run`.

### Docker
#### Build
```sh
docker build -t <TAG>:<VERSION> <CHEMIN_DOCKERFILE>
docker build -t tpseai:ex3 .
```

#### Run
```sh
docker run -p <port_server>:<port_container> <TAG>:<VERSION>
docker run -p 8080:3000 tpseai:ex3
```

Pour ajouter un volume
```sh
docker run -v <chemin_server>:<chemin_container> <TAG>:<VERSION>
docker run -v ~/tpseai/ex4/logs:/app/logs tpseai:ex4
```

#### Lancer un terminal _dans_ un container
Souvent utile pour voir exactement ce qu'il y a dans le container. Par exemple, aller vérifier la localisation d'un fichier créer par l'API.
```sh
docker exec -it <nom_du_container> sh
```
Pour obtenir le nom du container, utiliser la commande `docker ps`.

#### Copier un fichier vers/depuis un container
Pour spécifier le chemin du côté container, que ce soit la source ou la destination, la syntaxe est `<nom_du_container>:<chemin_dans_le_container>`.
```sh
docker cp <source> <destination>
docker cp <container name>:/app/logs/translations.jsonl ./logs
```

[Docker CLI Cheat Sheet](https://docs.docker.com/get-started/docker_cheatsheet.pdf)

### Kubernetes
#### Appliquer un template
```sh
kubectl apply -f template.yaml
```

#### Supprimer les ressources définies dans un template
```sh
kubectl delete -f template.yaml
```

#### Lister les ressources
```sh
kubectl get <ressource>
kubectl get pods
kubectl get services
kubectl get deployments
...
```

#### Port-forward une ressource (pod, service)
```sh
kubectl port-forward <ressource> <port_serveur>:<port_ressource>
kubectl port-forward service/translator-service 3000:80
```

#### Scale un déploiement/statefulset
```sh
kubectl scale --replicas=3 deployment/translator-deployment
```

[Kubectl Cheat Sheet](https://kubernetes.io/fr/docs/reference/kubectl/cheatsheet/)
