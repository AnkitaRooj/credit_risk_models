# Credit Risk Analytics Project

<!-- <video controls src="giphy_.mp4" title="<video controls src="giphy_.mp4" title="Title"></video>"></video> -->
<!-- ![My Project Demonstration GIF](images/giphy_.gif) -->

<!-- <img src="https://github.com/AnkitaRooj/credit_risk_models/blob/main/giphy_.mp4" width="400" height="300" alt="Demo"> -->

https://github.com/user-attachments/assets/199d70b6-9bdb-476d-948a-e8c5472d4033


## Overview
This project implements an automated credit risk assessment system with CI/CD pipeline integration. The system uses machine learning to evaluate credit risks while maintaining high code quality and automated testing standards.

## Project Structure
```
credit_risk_models/
├── .github/
│   └── workflows/
│       └── main.yaml
├── tests/
│   └── test_model.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Features
- Automated credit risk assessment model
- CI/CD pipeline using GitHub Actions
- Containerized deployment with Docker
- Automated testing suite
- Code quality enforcement

## Technologies
- Python 3.9
- GitHub Actions
- Docker
- pytest
- flake8

## Getting Started

### Prerequisites
- Python 3.9+
- Docker
- Git

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/credit_risk_models.git

# Navigate to project directory
cd credit_risk_models

# Install dependencies
pip install -r requirements.txt
```

### Running with Docker
```bash
# Build and run the container
docker-compose up --build
```

## CI/CD Pipeline
The project includes a comprehensive CI/CD pipeline that:
- Automatically runs on push to main branch and pull requests
- Performs automated testing
- Checks code quality
- Manages deployment

### Pipeline Steps
1. Code checkout
2. Test file preparation
3. Python environment setup
4. Dependency installation
5. Test execution
6. Code quality checks
7. Deployment (on main branch)

## Development

### Running Tests
```bash
pytest
```

### Code Quality
```bash
flake8 . --count --max-line-length=120 --statistics
```

Project Link: [https://github.com/yourusername/credit_risk_models](https://github.com/yourusername/credit_risk_models)



