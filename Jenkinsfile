pipeline {
    agent any

    stages {

        stage('Setup Virtual Environment') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'pytest'
            }
        }

        stage('Start Flask App with Waitress') {
            steps {
                bat 'venv\\Scripts\\activate && start /B waitress-serve --host=127.0.0.1 --port=8000 app:app'
                sleep 5
            }
        }

        stage('Verify Server is Running') {
            steps {
                bat 'curl -I http://127.0.0.1:8000' 
            }
        }

    }

    post {
        always {
            echo 'Stopping Waitress Server...'
            bat 'taskkill /F /IM python.exe'
        }
        success {
            echo 'Deployment Successful! 🎉'
        }
        failure {
            echo 'Deployment Failed ❌'
        }
    }
}
