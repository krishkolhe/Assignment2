pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/YOUR_USERNAME/YOUR_REPO.git'
            }
        }

        stage('Set Up Python') {
            steps {
                script {
                    sh 'python -m venv venv'
                    sh 'source venv/bin/activate'
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Migrations') {
            steps {
                script {
                    sh 'python manage.py migrate'
                }
            }
        }

        stage('Run Server') {
            steps {
                script {
                    sh 'python manage.py runserver 0.0.0.0:8000 &'
                }
            }
        }
    }
}
