# cloud-run-python-service-template

Reference implementation for a containerized Python HTTP service deployed on Google Cloud Run.

This repository is designed as a reusable starting point for small service endpoints that need a simple execution model, clear routing, container packaging, and a straightforward deployment path to Cloud Run. It separates route registration from handler logic and keeps the application footprint intentionally small so it can be extended with domain-specific behavior.

The current implementation includes example CRUD-style endpoints, local Docker execution, and a GitHub Actions workflow for build, test, and deployment.

## What This Repository Provides

- A minimal Flask-based HTTP service structure
- Route-per-operation handlers organized in a dedicated module folder
- Docker packaging for consistent local and cloud execution
- A CI/CD workflow targeting Google Cloud Run
- A simple base that can be adapted for internal tools, lightweight APIs, or service integrations

## Current Scope

This repository currently focuses on service structure and deployment flow. The handler implementations are intentionally lightweight and return example JSON responses without persistence, validation layers, or external system integration.

## Architecture Overview

- `app.py` exposes the HTTP routes and maps each endpoint to a dedicated handler
- `funcoes/` contains the operation-specific request handlers
- `Dockerfile` packages the service for container-based execution
- `.github/workflows/cicd.yml` defines the build, test, and deployment workflow for Cloud Run

## Project Structure

```text
.
|-- .github/
|   |-- ISSUE_TEMPLATE/
|   |-- PULL_REQUEST_TEMPLATE/
|   `-- workflows/
|       `-- cicd.yml
|-- funcoes/
|   |-- alterar.py
|   |-- cadastrar.py
|   `-- deletar.py
|-- app.py
|-- CONTRIBUTING.md
|-- Dockerfile
|-- LICENSE
|-- README.md
|-- requirements.txt
`-- test_app.py
```

## HTTP Endpoints

The current service exposes three example endpoints:

- `POST /cadastrar`
- `PUT /alterar`
- `DELETE /deletar`

These endpoints demonstrate the repository structure and request-handling pattern that can be reused for additional operations.

## Run Locally With Docker

Build the image:

```powershell
docker build -t cloud-run-python-service-template:latest .
```

Run the container:

```powershell
docker run -p 8080:8080 cloud-run-python-service-template:latest
```

The service will be available at `http://localhost:8080`.

## Example Requests

Create:

```powershell
$body = @{ nome = "Joao"; idade = 30 } | ConvertTo-Json
Invoke-RestMethod -Uri http://localhost:8080/cadastrar -Method Post -Body $body -ContentType "application/json"
```

Update:

```powershell
$body = @{ nome = "Joao"; idade = 31 } | ConvertTo-Json
Invoke-RestMethod -Uri http://localhost:8080/alterar -Method Put -Body $body -ContentType "application/json"
```

Delete:

```powershell
$body = @{ nome = "Joao" } | ConvertTo-Json
Invoke-RestMethod -Uri http://localhost:8080/deletar -Method Delete -Body $body -ContentType "application/json"
```

## Deployment Model

This repository is prepared for deployment to Google Cloud Run using a container image built from the included `Dockerfile`.

Manual deployment flow:

```powershell
gcloud auth login
gcloud config set project YOUR_GCP_PROJECT_ID
gcloud builds submit --tag gcr.io/YOUR_GCP_PROJECT_ID/cloud-run-python-service-template
gcloud run deploy cloud-run-python-service-template --image gcr.io/YOUR_GCP_PROJECT_ID/cloud-run-python-service-template --platform managed --region us-central1 --allow-unauthenticated
```

Replace `YOUR_GCP_PROJECT_ID` with your Google Cloud project ID.

## CI/CD Workflow

The GitHub Actions workflow currently:

- installs Python dependencies
- builds the Docker image as a validation step
- runs the test suite
- deploys to Cloud Run on pushes to `main`, assuming the required Google Cloud secrets are configured

Required GitHub secrets:

- `GCP_SA_KEY`
- `GCP_PROJECT_ID`

## How To Extend This Template

Typical extension paths include:

- replacing the example handlers with domain-specific service logic
- adding input validation and error handling
- integrating persistence or external APIs
- expanding the test suite beyond the current baseline
- renaming endpoints and modules to match the target service domain

## Limitations

This repository should be treated as a lightweight reference base, not as a complete production framework. It does not currently include:

- persistence
- authentication or authorization
- schema validation
- structured logging or observability instrumentation
- environment-specific configuration management beyond the deployment workflow

## Contributing

Contributions that improve clarity, reusability, and deployment quality are welcome. See `CONTRIBUTING.md` for contribution guidelines.
