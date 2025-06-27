pipeline {
    agent any

    environment {
        IMAGE_NAME = 'my-django-app'
        CONTAINER_NAME = 'django-app'
        PORT = '8000'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/ioanasilas/django-clean.git'
            }
        }

        stage('Stop Old Container') {
            steps {
                script {
                    sh """
                    if docker ps -q -f name=\$CONTAINER_NAME; then
                        echo "Stopping existing container..."
                        docker stop \$CONTAINER_NAME || true
                        docker rm \$CONTAINER_NAME || true
                    fi
                    """
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t \$IMAGE_NAME ."
            }
        }

        stage('Run Container') {
            steps {
                sh "docker run -d --name \$CONTAINER_NAME -p \$PORT:\$PORT \$IMAGE_NAME"
            }
        }

        stage('Migrate DB') {
            steps {
                sh 'docker exec django-app python manage.py migrate'
            }
        }


        stage('Wait & Health Check') {
            steps {
                script {
                    sleep(time: 5, unit: 'SECONDS')
                    sh "curl -f http://localhost:\$PORT || (echo 'Health check failed!' && exit 1)"
                }
            }
        }

        stage('Post-Deploy Info') {
            steps {
                echo "Deployed successfully at http://localhost:${PORT}"
            }
        }
    }

    post {
        failure {
            echo "Build or deploy failed!"
        }
        success {
            echo "All good! Jenkins pipeline finished successfully."
        }
        // Uncomment this block to stop and remove the container after every run
        // failure should not break build
        /*
        always {
            echo "Optional cleanup after pipeline run..."
            sh '''
            docker stop $CONTAINER_NAME || true
            docker rm $CONTAINER_NAME || true
            '''
        }
        */
    }
}
