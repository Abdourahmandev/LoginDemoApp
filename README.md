# LoginDemoApp

Application web de démonstration d'authentification utilisant **FastAPI**, **PostgreSQL** et **Streamlit**, orchestrée avec **Docker Compose**.

## Architecture

```
my-app/
├── docker-compose.yml
├── api/                  # Backend FastAPI
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
└── frontend/             # Interface Streamlit
    ├── Dockerfile
    ├── app.py
    └── requirements.txt
```

## Services

| Service    | Image / Build   | Port  | Rôle                        |
|------------|-----------------|-------|-----------------------------|
| `postgres` | postgres:15     | —     | Base de données              |
| `api`      | ./api           | 8000  | API REST (FastAPI)           |
| `frontend` | ./frontend      | 8501  | Interface utilisateur        |

## Prérequis

- [Docker](https://www.docker.com/) et Docker Compose installés

## Lancer l'application

```bash
docker compose up --build
```

- Interface utilisateur : http://localhost:8501
- Documentation API : http://localhost:8000/docs

## Fonctionnalités

### Créer un compte
- Saisissez un nom d'utilisateur et un mot de passe
- Cliquez sur **"Créer mon compte"**
- Un message de confirmation s'affiche si le compte est créé avec succès

### Se connecter
- Saisissez vos identifiants
- Cliquez sur **"Se connecter"**
- Un message de bienvenue s'affiche en cas de succès

## Endpoints API

| Méthode | Route       | Description                          |
|---------|-------------|--------------------------------------|
| POST    | `/register` | Créer un nouvel utilisateur          |
| POST    | `/login`    | Vérifier les identifiants            |

### Exemple de requête `/register`

```json
{
  "username": "alice",
  "password": "monmotdepasse"
}
```

### Exemple de requête `/login`

```json
{
  "username": "alice",
  "password": "monmotdepasse"
}
```

Réponse :
```json
{ "success": true }
```

## Variables d'environnement

| Variable       | Valeur par défaut                              |
|----------------|------------------------------------------------|
| `POSTGRES_DB`  | `mydb`                                         |
| `POSTGRES_USER`| `user`                                         |
| `POSTGRES_PASSWORD` | `password`                                |
| `DATABASE_URL` | `postgresql://user:password@postgres:5432/mydb`|

## Arrêter l'application

```bash
docker compose down
```

Pour supprimer également les données persistantes :

```bash
docker compose down -v
```
