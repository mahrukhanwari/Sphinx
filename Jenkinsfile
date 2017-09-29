pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'echo step 1'
		sh 'python --version'
		sh 'echo step1 ended'
		sh 'new Line#1'
		sh 'python pytest.py'
            }
        }
    }
	
	post {
		always {
			sh   'echo now clean up this thing'
		deleteDir()}
	}
}
