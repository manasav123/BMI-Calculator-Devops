pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t bmi-calculator:latest .'
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker rm -f bmi-app >nul 2>&1 || echo No existing container'
                bat 'docker run -d -p 5000:5000 --name bmi-app bmi-calculator:latest'
            }
        }
    }
}