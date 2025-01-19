pipeline {
    agent any

    stages {

        stage('Setup Virtual Environment') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate && pip install --upgrade pip'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'venv\\Scripts\\activate && pytest tests/'
            }
        }

        stage('Start Flask App with Waitress') {
            steps {
                bat 'venv\\Scripts\\activate && waitress-serve --host=127.0.0.1 --port=8000 app:app'
            }
        }

    }

    post {
        success {
            echo 'Deployment Successful! 🎉'
        }
        failure {
            echo 'Deployment Failed ❌'
        }
    }
}
