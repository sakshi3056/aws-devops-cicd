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
                sh '''
                    python3 -m venv .venv
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

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t experiment4-app:${BUILD_NUMBER} .'
            }
        }

        stage('Deploy Container') {
            steps {
                echo 'Deploying application container...'
                sh '''
                    docker rm -f experiment4-web || true
                    docker run -d --restart unless-stopped \
                        --name experiment4-web \
                        -p 8081:5000 \
                        experiment4-app:${BUILD_NUMBER}
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'curl --fail --retry 5 --retry-delay 2 http://127.0.0.1:8081/health'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: CI/CD pipeline completed!'
        }
        failure {
            echo 'FAILURE: Check Console Output.'
        }
        always {
            echo 'Pipeline execution finished.'
        }
    }
}
