# Email Marketing Campaign System

## Overview

This project is a scalable Email Marketing Campaign System built using microservices architecture on Google Cloud Platform (GCP). It allows scheduling and sending marketing emails, managing users and campaigns, and tracking email opens and clicks.

### Tech Stack

| Component         | Tool/Technology                   |
|-------------------|---------------------------------|
| Language          | Python (FastAPI)                 |
| Microservices     | User, Campaign, Emailer          |
| CI/CD             | Google Cloud Build + GitHub Triggers |
| Orchestration     | Kubernetes (GKE) (planned)       |
| Storage           | Firestore + Cloud Storage        |
| Monitoring        | Stackdriver + Alerting           |
| Email Provider    | Mailgun / SendGrid API (mocked) |

---

## Prerequisites

- Docker installed on your machine
- Google Cloud account with GKE and Cloud Build enabled (for deployment)
- Git installed
- Valid sender email credentials (for sending emails)

---

## Getting Started Locally (Email Service)

### 1. Clone the repository

```bash
git clone https://github.com/aloksharma-1/email-campaign-system.git
cd email-campaign-system/email-service 

2. Build the Docker image
docker build -t email-service:dev .

3. Run the Docker container
Replace the environment variables below with your sender email and password.
docker run -p 8000:8000 \
  -e SENDER_EMAIL=your_email@example.com \
  -e SENDER_PASSWORD=your_password \
  email-service:dev
4. Access the API
Open your browser or API client and visit:
http://localhost:8000

Run Terraform Commands
cd terraform

terraform init

terraform plan

terraform apply
Note: If you face quota issues related to SSD disk size, reduce disk_size_gb or number of nodes.

Git Workflow & Handling Large Files
Common Git Commands
git add .
git commit -m "Your commit message"
git push origin main

Handling Large Files Issue (Terraform Providers)
Add .terraform folder to .gitignore to avoid committing provider binaries:

terraform/.terraform/
terraform/terraform.tfstate
terraform/terraform.tfstate.backup
Remove cached .terraform folder if already added:


git rm -r --cached terraform/.terraform
git commit -m "Remove terraform provider binaries from repo"
git push origin main
If files exceed GitHub's 100MB limit, use Git LFS.

Environment Variables for Email Service
Variable	Description
SENDER_EMAIL	Sender's email address (e.g. Gmail)
SENDER_PASSWORD	Password or App password for sender email

