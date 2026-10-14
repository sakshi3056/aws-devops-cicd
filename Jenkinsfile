pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Creating Python virtual environment...'
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python --version
                    .venv/bin/python -m pip --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh '''
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install -r app/requirements.txt
                    .venv/bin/python -m pip install pytest
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests...'
                sh '.venv/bin/python -m pytest tests/ -v'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: CI Pipeline completed successfully!'
        }

        failure {
            echo 'FAILURE: Check Console Output for errors.'
        }

        always {
            echo 'CI Pipeline execution finished.'
        }
    }
}
