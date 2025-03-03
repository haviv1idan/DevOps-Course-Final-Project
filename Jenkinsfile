pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "haviv1idan/dev_sec_ops_course"
    }

    stages {
        stage('Checkout Repository') {
            steps {
                checkout scm
            }
        }

        stage('Read Version from File') {
            steps {
                script {
                    def version = sh(script: "cat flask_app/src/version.txt", returnStdout: true).trim()
                    env.APP_VERSION = version
                    echo "Version: ${env.APP_VERSION}"
                }
            }
        }

        stage('Set Build Tag') {
            when {
                anyOf {
                    branch 'main'
                    branch 'develop'
                    branch 'checking_jenkins_build'
                }
            }
            steps {
                script {
                    if (env.BRANCH_NAME == 'main') {
                        env.BUILD_TAG = "Main-flask-app-${env.APP_VERSION}-${env.BUILD_NUMBER}"
                    } else if (env.BRANCH_NAME == 'develop') {
                        env.BUILD_TAG = "Dev-flask-app-${env.APP_VERSION}-${env.BUILD_NUMBER}"
                    } else {
                        env.BUILD_TAG = "Test-flask-app-${env.APP_VERSION}-${env.BUILD_NUMBER}"
                    }
                    echo "Using Build Tag: ${env.BUILD_TAG}"
                }
            }
        }

        // stage('Install Dependencies') {
        //     steps {
        //         sh 'pip install flake8'
        //         sh 'pip install -r flask_app/src/requirements.txt'
        //         sh 'pip install -r python_server/src/requirements.txt'
        //     }
        // }

        // stage('Lint') {
        //     steps {
        //         sh 'flake8 --ignore=E501 --exclude venv,python_server/src/trivia_db.py'
        //     }
        // }

        // stage('Unit Test') {
        //     steps {
        //         sh 'python3 -m unittest discover -s flask_app/tests -v'
        //     }
        // }

        stage('Build Docker Image') {
            agent any 
            when {
                anyOf {
                    branch 'main'
                    branch 'develop'
                    branch 'checking_jenkins_build'
                }
            }
            steps {
                script {
                    echo "Current directory: ${pwd()}"
                    sh 'ls'
                    sh "cd flask_app"
                    echo "Current directory: ${pwd()}"
                    sh 'ls'
                    echo "Current directory after cd: ${pwd()}"
                    sh "docker build -t ${DOCKER_IMAGE}:${env.BUILD_TAG} -f Dockerfile ."
                }
            }
        }

        stage('Run Docker Container') {
            when {
                anyOf {
                    branch 'main'
                    branch 'develop'
                    branch 'checking_jenkins_build'
                }
            }
            steps {
                script {
                    sh "docker run -d --rm -p 5000:5000 ${DOCKER_IMAGE}:${env.BUILD_TAG}"
                }
            }
        }

        stage('Push to DockerHub') {
            when {
                anyOf {
                    branch 'main'
                    branch 'develop'
                    branch 'checking_jenkins_build'
                }
            }
            steps {
                script {
                    sh "docker push ${DOCKER_IMAGE}:${env.BUILD_TAG}"
                }
            }
        }
    }
}
