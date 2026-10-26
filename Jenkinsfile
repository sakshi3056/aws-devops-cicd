
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Source code checked out successfully.'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install -r app/requirements.txt
                    .venv/bin/python -m pip install pytest
                '''
            }
        }

        stage('Test') {
            steps {
                sh '.venv/bin/python -m pytest tests/ -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t experiment4-app:${BUILD_NUMBER} .'
            }
        }

        stage('Deploy Container') {
            steps {
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
                sh '''
                    curl --fail --retry 10 --retry-delay 2 \
                        http://host.docker.internal:8081/health
                '''
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
