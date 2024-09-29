pipeline {
    agent any
    environment {
        PATH = "$PATH:C:\\Python\\Scripts;C:\\Python"
    }
    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/Mdzaidsiddique/Flipkart-Sounds-Scenario-test.git', branch: 'main'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat '''
                    echo Checking Python and Pip versions...
                    python --version
                    pip --version
                    echo Installing dependencies...
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                // Run Behave with Allure report generation
                bat 'behave -f allure_behave.formatter:AllureFormatter -o allure-results'

            }
        }
    }
    post {
        always {
            echo 'Cleaning up workspace'
            cleanWs()
            echo 'Archiving Allure reports...'
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
        success {
            echo 'Build succeeded, tests passed!'
        }
        failure {
            echo 'Build failed, please check the logs.'
        }
    }
}
