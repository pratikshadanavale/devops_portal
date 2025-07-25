pipeline {
    agent any

    environment {
        PYTHON_PATH = 'C:\\Users\\pratiksha\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
        VENV_DIR = '.venv'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git credentialsId: 'github-creds-pratiksha', url: 'https://github.com/pratikshadanavale/devops_portal.git'
            }
        }

        stage('Set up Virtual Environment') {
            steps {
                bat "${PYTHON_PATH} -m venv %VENV_DIR%"
                bat "%VENV_DIR%\\Scripts\\python -m pip install --upgrade pip"
            }
        }

        stage('Install Requirements') {
            steps {
                bat ".venv\\Scripts\\pip install -r requirements.txt"

            }
        }

        stage('Django Check') {
            steps {
                bat "%VENV_DIR%\\Scripts\\python manage.py check"
            }
        }

        stage('Run Tests') {
            steps {
                bat '.venv\\Scripts\\python manage.py test'
            }
        }

        stage('Send CI Log to API') {
            steps {
                bat ".venv/Scripts/python send_report.py"

            }
        }

        stage('Jira Link') {
            steps {
                echo '🔗 Jira Ticket: SATMS-008 - Integrate DevOps CI log with Django Portal'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline successful. Ready to close the Jira ticket.'
        }
        failure {
            echo '❌ Pipeline failed. Please check Jenkins logs.'
        }
    }
}
