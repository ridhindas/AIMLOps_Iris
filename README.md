# AIMLOps Iris Classification

An end-to-end **MLOps + DevSecOps pipeline** for an Iris classification machine-learning API built with **Python, Scikit-learn, FastAPI, Docker, GitHub Actions, Trivy, and OWASP ZAP**.

The project automates model training, validation, application testing, containerization, security scanning, deployment testing, and security reporting through GitHub Actions.

---

## 🚀 Project Overview

This project demonstrates how a machine-learning application can be developed and delivered using modern MLOps and DevSecOps practices.

The application:

* Trains a Random Forest classifier using the Iris dataset.
* Stores the trained model as a serialized `model.pkl` artifact.
* Exposes the model through a FastAPI REST API.
* Packages the application into a Docker image.
* Validates model accuracy automatically.
* Runs automated application tests.
* Performs Python security analysis using Bandit.
* Scans Python dependencies using pip-audit.
* Scans the Docker image using Trivy.
* Performs API security testing using OWASP ZAP.
* Generates security reports as GitHub Actions artifacts.
* Performs containerized deployment testing inside GitHub Actions.

---

# 🏗️ Architecture

```text
                        ┌──────────────────────┐
                        │      Developer       │
                        │   Code / Model Code  │
                        └──────────┬───────────┘
                                   │
                                   │ git push
                                   ▼
                        ┌──────────────────────┐
                        │       GitHub         │
                        │      Repository      │
                        └──────────┬───────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │       GitHub Actions        │
                    │          CI Pipeline        │
                    └──────────────┬──────────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              │                    │                    │
              ▼                    ▼                    ▼
       Train Model          Validate Model         Run Tests
              │                    │                    │
              └────────────────────┼────────────────────┘
                                   │
                                   ▼
                         Security Analysis
                       ┌───────────┴───────────┐
                       │                       │
                    Bandit                pip-audit
                       │                       │
                       └───────────┬───────────┘
                                   │
                                   ▼
                           CI Success
                                   │
                                   ▼
                    ┌──────────────────────────┐
                    │       CD Pipeline        │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                         Train / Validate Model
                                 │
                                 ▼
                         Build Docker Image
                                 │
                                 ▼
                         Trivy Image Scan
                                 │
                                 ▼
                        Start API Container
                                 │
                         ┌───────┴────────┐
                         ▼                ▼
                    Health Check    Prediction Test
                         │                │
                         └───────┬────────┘
                                 ▼
                         OWASP ZAP Scan
                                 │
                                 ▼
                       Security Reports
                                 │
                                 ▼
                          Cleanup
```

---

# 📂 Project Structure

```text
AIMLOps_Iris/
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
│
├── models/
│   └── model.pkl
│
├── security/
│   ├── bandit/
│   ├── pip-audit/
│   ├── trivy/
│   └── zap/
│
├── tests/
│   └── test_app.py
│
├── app.py
├── retrain.py
├── validate_model.py
├── requirements.txt
├── requirements-dev.txt
├── Dockerfile
├── .gitignore
└── README.md
```

---

# 🧰 Technology Stack

| Technology     | Purpose                             |
| -------------- | ----------------------------------- |
| Python 3.11    | Application and ML development      |
| Scikit-learn   | Machine-learning model              |
| Iris Dataset   | Training dataset                    |
| Random Forest  | Classification algorithm            |
| FastAPI        | REST API                            |
| Uvicorn        | ASGI application server             |
| Pydantic       | API request validation              |
| Joblib         | Model serialization                 |
| Docker         | Application containerization        |
| GitHub Actions | CI/CD automation                    |
| Bandit         | Python security scanning            |
| pip-audit      | Dependency vulnerability scanning   |
| Trivy          | Docker image vulnerability scanning |
| OWASP ZAP      | API/web security testing            |
| Pytest         | Automated testing                   |

---

# 🤖 Machine Learning Model

The project uses the classic **Iris dataset** from Scikit-learn.

The model is a:

```text
RandomForestClassifier
```

Configuration:

```text
n_estimators = 100
random_state = 42
```

The model predicts one of three Iris species classes:

```text
0 → Iris Setosa
1 → Iris Versicolor
2 → Iris Virginica
```

The model expects exactly four input features:

```text
Sepal Length
Sepal Width
Petal Length
Petal Width
```

---

# 🔄 MLOps Workflow

The model lifecycle follows this process:

```text
Training Data
     │
     ▼
Model Training
     │
     ▼
model.pkl
     │
     ▼
Model Validation
     │
     ▼
Automated Tests
     │
     ▼
Docker Image
     │
     ▼
Security Scanning
     │
     ▼
API Deployment Test
```

Model validation is performed using the complete Iris dataset.

The minimum required accuracy is:

```text
0.90
```

The pipeline fails if the model accuracy is below this threshold.

---

# 🔐 DevSecOps Pipeline

Security checks are integrated into the CI/CD workflow.

## 1. Bandit

Bandit performs static security analysis of Python source code.

The pipeline generates:

```text
bandit-report.json
```

The report is uploaded as a GitHub Actions artifact.

---

## 2. pip-audit

`pip-audit` checks Python dependencies for known vulnerabilities.

The generated report is:

```text
pip-audit-report.json
```

The report is uploaded to GitHub Actions.

---

## 3. Trivy

Trivy scans the built Docker image for vulnerabilities.

The pipeline scans for:

```text
HIGH
CRITICAL
```

A JSON report is generated:

```text
iris-mlops-api.json
```

The report is uploaded as a GitHub Actions artifact.

> The current pipeline performs the Trivy scan in a containerized Trivy environment.

---

## 4. OWASP ZAP

OWASP ZAP performs a baseline security scan against the running FastAPI application.

The pipeline generates:

```text
zap-report.html
zap-report.json
```

These reports can be downloaded from the GitHub Actions workflow artifacts.

---

# 🔁 CI Pipeline

The CI pipeline is triggered when code is pushed to `main` or when a pull request targets `main`.

The CI workflow performs:

```text
Checkout
   ↓
Setup Python
   ↓
Install Dependencies
   ↓
Train Model
   ↓
Validate Model
   ↓
Run Pytest
   ↓
Bandit Scan
   ↓
pip-audit
   ↓
Verify Model Artifact
   ↓
Upload Model Artifact
```

The CI pipeline also uploads the trained model as a GitHub Actions artifact.

Artifact:

```text
iris-model
```

---

# 🚢 CD Pipeline

The CD pipeline runs after the CI pipeline completes successfully.

The deployment pipeline performs:

```text
Checkout
   ↓
Setup Python
   ↓
Install Dependencies
   ↓
Train Model
   ↓
Validate Model
   ↓
Build Docker Image
   ↓
Export Docker Image
   ↓
Trivy Scan
   ↓
Start API Container
   ↓
Health Check
   ↓
Prediction Test
   ↓
OWASP ZAP Scan
   ↓
Upload Security Reports
   ↓
Cleanup
```

---

# 🐳 Docker

The application is packaged as a Docker image.

Build the image locally:

```bash
docker build -t iris-mlops-api:latest .
```

Check the image:

```bash
docker images iris-mlops-api
```

---

# ▶️ Run Locally

Start the container:

```bash
docker run -d \
  --name iris-api \
  -p 8000:8000 \
  iris-mlops-api:latest
```

Check the container:

```bash
docker ps
```

---

# ❤️ Health Check

Open:

```text
http://localhost:8000/health
```

Expected response:

```json
{
  "status": "healthy",
  "model_loaded": true,
  "version": "1.0.0"
}
```

---

# 🔮 Prediction API

## Endpoint

```text
POST /predict
```

Example request:

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features":[5.1,3.5,1.4,0.2]}'
```

Example response:

```json
{
  "model_version": "1.0.0",
  "prediction": 0
}
```

---

# 📖 API Documentation

FastAPI automatically provides interactive API documentation.

Swagger UI:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

---

# 🧪 Running Tests Locally

Create a Python virtual environment:

```bash
python -m venv venv
```

Activate it on Linux/MobaXterm:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

Run tests:

```bash
pytest -v
```

---

# 🤖 Train the Model Locally

Run:

```bash
python retrain.py
```

Expected output:

```text
Fetching training data...
Training Random Forest model...
Model saved to models/model.pkl
```

---

# ✅ Validate the Model

Run:

```bash
python validate_model.py
```

Expected output:

```text
Model Accuracy: 1.0000
Model validation passed.
```

The pipeline requires an accuracy of at least:

```text
90%
```

---

# 🔍 Run Security Scans Locally

## Bandit

```bash
mkdir -p security/bandit

python -m bandit \
  -r . \
  -x ./venv,./tests \
  -f json \
  -o security/bandit/bandit-report.json
```

---

## pip-audit

```bash
mkdir -p security/pip-audit

pip-audit \
  -r requirements.txt \
  -f json \
  -o security/pip-audit/pip-audit-report.json
```

---

## Trivy

After building the Docker image:

```bash
docker run --rm \
  aquasec/trivy:latest \
  image \
  iris-mlops-api:latest \
  --severity HIGH,CRITICAL
```

---

# 🌐 API Security Testing with OWASP ZAP

Start the application:

```bash
docker run -d \
  --name iris-api \
  -p 8000:8000 \
  iris-mlops-api:latest
```

Run a ZAP baseline scan:

```bash
docker run --rm \
  --network host \
  -v "$(pwd)/security/zap:/zap/wrk:rw" \
  ghcr.io/zaproxy/zaproxy:stable \
  zap-baseline.py \
  -t http://localhost:8000 \
  -r zap-report.html \
  -J zap-report.json \
  -I
```

Reports will be generated under:

```text
security/zap/
```

---

# 📦 GitHub Actions Artifacts

The workflows generate security and ML artifacts.

Expected artifacts include:

```text
iris-model
bandit-report
pip-audit-report
trivy-image-report
zap-baseline-report
```

These artifacts can be downloaded from:

```text
GitHub Repository
        ↓
Actions
        ↓
Workflow Run
        ↓
Artifacts
```

---

# 🔒 Security Architecture

Security is integrated throughout the software lifecycle.

```text
Source Code
    │
    ├── Bandit
    │
    ▼
Dependencies
    │
    ├── pip-audit
    │
    ▼
Machine Learning Model
    │
    ├── Accuracy Validation
    │
    ▼
Docker Image
    │
    ├── Trivy
    │
    ▼
Running API
    │
    ├── OWASP ZAP
    │
    ▼
Security Reports
```

This follows a **shift-left security** approach where security testing is performed automatically during CI/CD rather than only after deployment.

---

# 🛡️ Container Security

The Docker container runs the FastAPI application using a non-root user.

The Dockerfile creates:

```text
mluser
```

and switches to:

```dockerfile
USER mluser
```

This reduces the security risk associated with running the application as `root`.

---

# ⚙️ GitHub Actions Workflows

The project contains two main workflows:

### CI

```text
.github/workflows/ci.yml
```

Responsible for:

* Model training
* Model validation
* Unit testing
* Bandit
* pip-audit
* Model artifact generation

### CD

```text
.github/workflows/cd.yml
```

Responsible for:

* Docker image creation
* Trivy scanning
* Container deployment testing
* API health testing
* Prediction testing
* OWASP ZAP scanning
* Security report generation
* Cleanup

---

# 🔄 Development Workflow

The recommended development workflow is:

```text
1. Modify source code
       ↓
2. Run tests locally
       ↓
3. Train/validate model
       ↓
4. Build Docker image
       ↓
5. Test API locally
       ↓
6. Commit changes
       ↓
7. Push to GitHub
       ↓
8. CI automatically runs
       ↓
9. CD runs after successful CI
       ↓
10. Security reports generated
```

---

# 📊 Pipeline Quality Gates

The pipeline verifies several conditions before considering the application successful.

### Model Quality

```text
Accuracy >= 90%
```

### Application Quality

```text
Pytest tests pass
```

### Model Artifact

```text
models/model.pkl exists
```

### API Health

```text
status = healthy
model_loaded = true
```

### Prediction

The `/predict` endpoint must successfully process a valid Iris feature vector.

### Security

The pipeline performs:

```text
Bandit
pip-audit
Trivy
OWASP ZAP
```

---

# 🧹 Container Cleanup

The CD pipeline automatically removes temporary resources after execution.

It cleans up:

```text
iris-api
iris-test-network
zap-test-network
Trivy temporary image archive
ZAP temporary reports
```

This keeps the GitHub Actions runner clean between workflow executions.

---

# 🎯 Project Goals

The main objectives of this project are:

* Demonstrate an end-to-end MLOps workflow.
* Automate machine-learning model training.
* Validate model quality automatically.
* Expose the model through a production-style REST API.
* Containerize the ML application.
* Implement CI/CD using GitHub Actions.
* Integrate DevSecOps security practices.
* Automate vulnerability scanning.
* Generate security reports.
* Perform API security testing.
* Demonstrate reproducible ML application deployment.

---

# 🚀 Future Improvements

The following improvements can be added as the project evolves:

* [ ] Use the exact validated CI model artifact in CD instead of retraining.
* [ ] Add Git commit SHA based Docker image tags.
* [ ] Enable Trivy as a deployment security gate.
* [ ] Add more comprehensive Pytest coverage.
* [ ] Generate a Docker SBOM using Trivy.
* [ ] Add model metadata and model versioning.
* [ ] Add experiment tracking using MLflow.
* [ ] Add model registry integration.
* [ ] Add automated model drift detection.
* [ ] Add staging and production environments.
* [ ] Add deployment approval for production.
* [ ] Add Kubernetes deployment.
* [ ] Add monitoring and observability.
* [ ] Add Prometheus/Grafana monitoring.

---

# 📌 Current Project Status

| Component                   | Status                 |
| --------------------------- | ---------------------- |
| Iris ML model               | ✅                      |
| Model training automation   | ✅                      |
| Model validation            | ✅                      |
| FastAPI API                 | ✅                      |
| Docker containerization     | ✅                      |
| GitHub Actions CI           | ✅                      |
| GitHub Actions CD           | ✅                      |
| Pytest                      | ✅                      |
| Bandit                      | ✅                      |
| pip-audit                   | ✅                      |
| Trivy                       | ✅                      |
| OWASP ZAP                   | ✅                      |
| Security reports            | ✅                      |
| Automated container testing | ✅                      |
| Model artifact workflow     | 🔄 Improvement planned |
| Model registry              | 🔄 Future              |
| Kubernetes deployment       | 🔄 Future              |
| Monitoring                  | 🔄 Future              |

---

# 👨‍💻 Author

**Ridhin Das**

GitHub:

```text
https://github.com/ridhindas
```

Project Repository:

```text
https://github.com/ridhindas/AIMLOps_Iris
```

---

# 📄 License

This project is intended for educational and demonstration purposes.

You may modify and extend it for your own MLOps and DevSecOps experiments.
