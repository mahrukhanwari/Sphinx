
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
		'echo now clean up this thing'
		deleteDir()}
	}
}
