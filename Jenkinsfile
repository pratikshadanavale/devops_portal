
pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/pratikshadanavale/devops_portal.git', branch: 'master'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat 'python -m venv %VENV_DIR%'
                bat '%VENV_DIR%\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Django Checks') {
            steps {
                bat '%VENV_DIR%\\Scripts\\python manage.py check'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat '%VENV_DIR%\\Scripts\\python manage.py test'
            }
        }

        stage('Send Report and Log CI Status') {
            steps {
                echo 'Running send_report.py to generate report and log to API'
                bat 'venv\\Scripts\\python.exe JenkinsProjects\\JenkinsEmailReport\\send_report.py'
            }
        }
    }

    post {
        success {
            echo '✅ CI pipeline passed!'
        }
        failure {
            echo '❌ CI failed. Check logs.'
        }
    }
}
