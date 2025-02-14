pipeline {
    agent {
        docker {
            image 'python:3.11-alpine'
            args '--user root'
        }
    }

    stages {
        stage('Checkout Repository') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'pip install flake8'
            }
        }

        stage('Lint') {
            steps {
                sh 'flake8 --exclude venv,python_server/trivia_db.py'
            }
        }
    }
}
