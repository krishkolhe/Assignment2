pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Agasya27/srceom-agasya-butolia-sl-2-Ass-2.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t agasya27/studentproject .'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    sh 'docker run agasya27/studentproject python manage.py test app1 app2'  // Run Django tests
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        sh 'echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'
                        sh 'docker tag agasya27/studentproject:latest "$DOCKER_USER/studentproject:latest"'
                        sh 'docker push agasya27/studentproject:latest'
                    }
                }
            }
        }
    }
}

