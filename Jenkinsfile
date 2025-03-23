pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Agasya27/srceom-agasya-butolia-sl-3-Ass-2.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t agasya27/studentproject .'
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    sh 'docker login -u agasya27 -p Agasya2005'
                    sh 'docker push agasya27/studentproject'
                }
            }
        }
    }
}
