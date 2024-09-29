pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from GitHub
                git branch: 'main', url: 'https://github.com/Mdzaidsiddique/Flipkart-Sounds-Scenario-test.git'
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
                // Run Behave tests
                script {
                    // Change to the directory where your features are located if needed
                    bat 'behave'
                }
            }
        }
    }

   post {
        always {
            echo 'Cleaning up workspace'
            cleanWs()
        }
        success {
            echo 'Build succeeded, tests passed!'
        }
        failure {
            echo 'Build failed, please check the logs.'
        }
    }
}
