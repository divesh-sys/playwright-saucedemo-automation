pipeline {
    agent any

    environment {
        PYTHON = PYTHON = 'C:\\Users\\MUR90411\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
    }

    options {
        timestamps()
        timeout(time: 30, unit: 'MINUTES')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install') {
            steps {
                bat 'if not exist .venv "%PYTHON%" -m venv .venv'
                bat '.venv\\Scripts\\python -m pip install --upgrade pip'
                bat '.venv\\Scripts\\pip install -r requirements.txt'
                bat '.venv\\Scripts\\playwright install'
            }
        }

        stage('Lint') {
            steps {
                bat '.venv\\Scripts\\ruff check .'
            }
        }

        stage('Test') {
            steps {
                bat '.venv\\Scripts\\pytest --browser chromium --browser firefox --browser webkit --junitxml=reports/junit.xml'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/junit.xml'
            archiveArtifacts artifacts: 'reports/**, test-results/**, allure-results/**', allowEmptyArchive: true
        }
    }
}