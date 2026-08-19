# 🧠 BrainCheck

A minimal Flask quiz application built exclusively to demonstrate Docker, CI/CD with GitHub Actions, and automated testing.

> The application itself is intentionally simple. The focus is on deployment automation, not application features.

## Project Overview

BrainCheck is a 5-question multiple-choice quiz app. It demonstrates:

- **Containerization** with Dockerfile and Docker Compose
- **CI/CD Pipeline** with GitHub Actions
- **Automated Testing** with pytest
- **One-Command Deployment** with `docker compose up`

## Objectives

| Objective | How It Is Demonstrated |
| --- | --- |
| Automatic deployment | `docker compose up` runs the app |
| Deployment automation | Dockerfile and Compose handle setup |
| CI/CD pipeline | GitHub Actions tests and builds on every push |
| Automated testing | pytest validates routes, scoring, and health checks |

## Technology Stack

| Technology | Version | Purpose |
| --- | --- | --- |
| Python | 3.13 | Runtime |
| Flask | 3.1.1 | Web framework |
| pytest | 8.3.5 | Testing |
| Docker | Latest | Containerization |
| Docker Compose | Latest | Orchestration |
| GitHub Actions | - | CI/CD |

## Folder Structure

```text
BRAINCHECK/
|-- app.py                    # Flask application
|-- requirements.txt          # Python dependencies
|-- Dockerfile                # Docker image definition
|-- docker-compose.yml        # Docker Compose config
|-- .dockerignore             # Docker build exclusions
|-- .gitignore                # Git exclusions
|-- README.md                 # Project documentation
|-- home.html                 # Landing page
|-- quiz.html                 # Quiz page
|-- result.html               # Score display
|-- style.css                 # Stylesheet
|-- tests/test_app.py         # Automated tests
`-- .github/workflows/ci.yml  # GitHub Actions pipeline
```

## How to Run

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed on your machine

### Quick Start

```powershell
git clone https://github.com/harshkumar07423/DevOps--project.git
cd DevOps--project
docker compose up --build
```

Open [http://localhost:5000](http://localhost:5000/) in your browser.

### Stop the Application

```powershell
docker compose down
```

## Docker Commands

| Command | Description |
| --- | --- |
| `docker compose up --build` | Build and start the app |
| `docker compose up -d` | Start in detached mode |
| `docker compose down` | Stop and remove containers |
| `docker compose logs` | View application logs |
| `docker compose ps` | Check container status |
| `docker build -t braincheck .` | Build the image manually |
| `docker run -p 5000:5000 braincheck` | Run the container manually |

## GitHub Actions

The CI pipeline in `.github/workflows/ci.yml` runs on every push and pull request. It checks out the repository, installs dependencies, runs pytest, and validates the application.

## Testing

```powershell
py -m pip install -r requirements.txt
py -m pytest tests/ -v
```

The test suite covers the home page, quiz rendering, result scoring, and health endpoint.

## Future Scope

- Multi-stage Docker builds
- Docker volumes with SQLite
- Staging and production configurations
- Nginx reverse proxy
- Prometheus and Grafana monitoring
- Docker Hub or GHCR image publishing
- Terraform, Ansible, or Kubernetes deployment

## License

This project is for educational purposes.

Built to learn DevOps.