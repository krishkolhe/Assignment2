pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/yourusername/StudentProject.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t yourdockerhubusername/studentproject .'
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    sh 'docker login -u yourdockerhubusername -p yourpassword'
                    sh 'docker push yourdockerhubusername/studentproject'
                }
            }
        }
    }
}
