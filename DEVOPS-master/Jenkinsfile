pipeline {
    agent any

    environment {
        IMAGE_NAME = 'flask-todo-app'
        CONTAINER_NAME = 'flask-todo-container'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/likith8/DEVOPS.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    // Stop and remove any existing container with the same name
                    sh "docker rm -f ${CONTAINER_NAME} || true"

                    // Run the container with specified name and .env file
                    sh "docker run -d --name ${CONTAINER_NAME} -p 5000:5000 --env-file .env ${IMAGE_NAME}"
                }
            }
        }

        stage('Test (Optional)') {
            steps {
                script {
                    // Run pytest inside the running container
                    sh "docker exec ${CONTAINER_NAME} pytest tests/"
                }
            }
        }
    }

    post {
        always {
            echo "Container and image are preserved. No cleanup is performed."
        }
    }
}
