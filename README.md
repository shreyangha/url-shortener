# URL Shortener – Dockerized Backend with Redis

A production-style URL shortener built using Flask, Redis, Docker, and Docker Compose.
This project demonstrates how to build a stateless backend service backed by a persistent datastore and orchestrated using containers.

---

## Architecture

Client  
→ Flask API (Gunicorn)  
→ Redis  

- The API is stateless and does not store data in memory  
- Redis persists URL mappings  
- Docker Compose manages multi-container orchestration  
- Services communicate using Docker’s internal networking  

---

## Tech Stack

- Python (Flask)
- Gunicorn
- Redis
- Docker
- Docker Compose
- Git & GitHub

---

## Project Structure

url-shortner/
├── api/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
└── README.md

---

## How to Run Locally

### Prerequisites
- Docker
- Docker Compose

### Start the application

docker compose up -d

This starts:
- API on http://localhost:5000
- Redis datastore

To stop all services:

docker compose down

---

## API Usage

### Create a Short URL

curl -X POST http://localhost:5000/shorten \
-H "Content-Type: application/json" \
-d '{"url":"https://example.com"}'

Example response:

{
  "short_url": "http://localhost:5000/AbC123"
}

---

### Redirect Using Short URL

curl -i http://localhost:5000/AbC123

Response:

HTTP/1.1 302 FOUND  
Location: https://example.com  

---

## Key Design Decisions

- Stateless API design
- Redis used for persistence
- Gunicorn used instead of Flask development server
- Docker Compose service-based networking

---

## Development Workflow

git status  
git add .  
git commit -m "Meaningful commit message"  
git push  

---

## Future Enhancements

- Add NGINX reverse proxy
- Persist Redis using Docker volumes
- Add health checks
- Add rate limiting
- Add CI/CD pipeline
- Deploy on Kubernetes

---

## Author

Shreyangha Sahu
