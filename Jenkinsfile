
pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                bat 'echo step 1'
		bat 'python --version'
		bat 'python pytest.py'
            }
        }
    }
	
	post {
		always {
		archive 'build/libs/**/*.jar'
		junit 'build/reports/**/*.xml'}
	}
}
