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

        stage('Unit Test') {
            agent {
                docker {
                    image 'python:3.11-alpine'
                    args '--user root'
                }
            }
            steps {
                script {
                    echo "Running tests inside a Docker container..."
                    sh 'pip install -r flask_app/src/requirements.txt'
                    sh 'python3 -m unittest discover -s flask_app/tests -v'
                }
            }
        }

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
                    sh "docker build -t ${DOCKER_IMAGE}:${env.BUILD_TAG} -f flask_app/src/Dockerfile ."
                    sh "docker build -t ${DOCKER_IMAGE}:${env.BUILD_TAG}-py -f python_server/src/Dockerfile ."
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
                    sh "docker push ${DOCKER_IMAGE}:${env.BUILD_TAG}-py"
                }
            }
        }
    }
}
