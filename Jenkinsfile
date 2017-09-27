pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'echo step 1'
		sh 'python --version'
		sh 'echo step1 ended'
		sh 'pull request generated from branch-a'
            }
        }
    }
	
	post {
		always {





sh   'echo now clean up this thing'
		deleteDir()}
	}
}
