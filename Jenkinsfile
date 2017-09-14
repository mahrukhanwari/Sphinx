
pipeline {
    agent { docker 'python:3.5.1' }
    stages {
        stage('build') {
            steps {
                bat 'echo step 1'
				bat 'python --version'
            }
        }
    }
}