pipeline {
    agent any

    environment {
        GITHUB_CREDENTIALS = credentials('github-credentials')  // Reference stored credentials
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    git credentialsId: 'github-credentials', url: 'https://github.com/YOUR_USERNAME/YOUR_REPO.git', branch: 'main'
                }
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

