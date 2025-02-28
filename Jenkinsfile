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
                sh 'pip install -r flask_app/src/requirements.txt'
                sh 'pip install -r python_server/src/requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                sh 'flake8 --exclude venv,python_server/trivia_db.py'
            }
        }

        stage('Unit Test') {
            steps {
                sh 'python3 -m unittest discover -s flask_app/tests -v'
            }
        }
    }
}
