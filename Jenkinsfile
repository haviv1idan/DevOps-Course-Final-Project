pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS = credentials('docker')
        REPOSITORY = "haviv1idan/dev_sec_ops_course"
        APP_IMAGE_NAME = 'flask_app'
        APP_CONTAINER_NAME = 'flask_app'
        SERVER_IMAGE_NAME = 'python_server'
        SERVER_CONTAINER_NAME = 'python_server'
    }

    stages {

        stage ('Checkout Code') {
            steps {
                checkout scm
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
                    sh 'pip install --no-cache-dir -r flask_app/src/requirements.txt'
                    sh 'python3 -m unittest discover -s flask_app/tests -v'
                }
            }
        }

        stage('Read Version from File') {
            steps {
                script {
                    def flask_version = sh(script: "cat flask_app/src/version.txt", returnStdout: true).trim()
                    env.APP_VERSION = flask_version
                    echo "Flask Version: ${env.APP_VERSION}"

                    def server_version = sh(script: "cat python_server/src/version.txt", returnStdout: true).trim()
                    env.SERVER_VERSION = server_version
                    echo "Python Server Version: ${env.SERVER_VERSION}"
                }
            }
        }

        stage('Set Build Tag') {
            steps {
                script {
                    if (env.BRANCH_NAME == 'main') {
                        env.SERVER_BUILD_TAG = "main-server-${env.SERVER_VERSION}-${env.BUILD_NUMBER}"
                        env.APP_BUILD_TAG = "main-app-${env.APP_VERSION}-${env.BUILD_NUMBER}"
                    } else if (env.BRANCH_NAME == 'develop') {
                        env.SERVER_BUILD_TAG = "dev-server-${env.SERVER_VERSION}-${env.BUILD_NUMBER}"
                        env.APP_BUILD_TAG = "dev-app-${env.APP_VERSION}-${env.BUILD_NUMBER}"
                    } else {
                        env.SERVER_BUILD_TAG = "test-server-${env.SERVER_VERSION}-${env.BUILD_NUMBER}"
                        env.APP_BUILD_TAG = "test-app-${env.APP_VERSION}-${env.BUILD_NUMBER}"
                    }
                    echo "Using Build Tag: ${env.APP_BUILD_TAG}"
                    echo "Using Build Tag: ${env.SERVER_BUILD_TAG}"
                }
            }
        }

        stage ('Build Docker Image') { 
            steps { 
                sh "docker build -t ${REPOSITORY}:${env.APP_BUILD_TAG} -f flask_app/Dockerfile ."
                sh "docker build -t ${REPOSITORY}:${env.SERVER_BUILD_TAG} -f python_server/src/Dockerfile ."
            }
        }

        stage ('Run Docker Container') {
            steps {
                sh "docker run -d -p 8000:8000 --name ${SERVER_CONTAINER_NAME}-${env.BUILD_NUMBER} ${REPOSITORY}:${env.SERVER_BUILD_TAG}"
                sh "docker run -d -p 59000:59000 --name ${APP_CONTAINER_NAME}-${env.BUILD_NUMBER} ${REPOSITORY}:${env.APP_BUILD_TAG}"
            }
        }

        stage ('Test') {
            steps {
                sh "docker exec ${APP_CONTAINER_NAME}-${env.BUILD_NUMBER} python3 -m unittest discover -s flask_app/tests -v"
            }
        }

        stage ('Login and Push Docker Images') {
            when {
                anyOf {
                    branch 'main'
                    branch 'develop'
                }
            }
            steps {
                script {
                    withDockerRegistry([credentialsId: 'docker', url: 'https://index.docker.io/v1/']) {
                        echo 'Logged in to Docker Hub'
                        sh "docker push ${REPOSITORY}:${env.APP_BUILD_TAG}"
                        sh "docker push ${REPOSITORY}:${env.SERVER_BUILD_TAG}"

                    }
                }
            }
        }

        stage ('Teardown') {
            steps {
                sh "docker stop ${APP_CONTAINER_NAME}-${env.BUILD_NUMBER} && docker rm ${APP_CONTAINER_NAME}-${env.BUILD_NUMBER}"
                sh "docker rmi ${REPOSITORY}:${env.APP_BUILD_TAG}"

                sh "docker stop ${SERVER_CONTAINER_NAME}-${env.BUILD_NUMBER} && docker rm ${SERVER_CONTAINER_NAME}-${env.BUILD_NUMBER}"
                sh "docker rmi ${REPOSITORY}:${env.SERVER_BUILD_TAG}"
            }
        }
    }    
}
