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
                dir('devops_portal/JenkinsEmailReport') {
                    bat "..\\..\\%VENV_DIR%\\Scripts\\pip install -r requirements.txt"
                }
            }
        }

        stage('Django Check') {
            steps {
                dir('devops_portal') {
                    bat "..\\%VENV_DIR%\\Scripts\\python manage.py check"
                }
            }
        }

        stage('Run Tests') {
            steps {
                dir('devops_portal') {
                    bat "..\\%VENV_DIR%\\Scripts\\pytest"
                }
            }
        }

        stage('Send CI Log to API') {
            steps {
                dir('devops_portal/JenkinsEmailReport') {
                    bat "..\\..\\%VENV_DIR%\\Scripts\\python send_report.py"
                }
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
