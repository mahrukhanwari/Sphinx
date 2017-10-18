pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'echo step 1'
		sh 'python --version'
		sh 'echo step1 ended'
		sh 'python pytest.py'
		sh 'echo BITA'
            }
        }
    }
	
	post {
		success {
		sh   'echo now clean up this thing'
		deleteDir()
		mail body: "View console output at  ${BUILD_URL}, subject: "${JOB_NAME} build# ${BUILD_NUMBER} SUCCESSFUL" , to: 'mahrukh.anwari@xflowresearch.com'
		}
		
		failure {
		sh   'echo now clean up this thing'
		deleteDir()
		mail body: "View console output at  ${BUILD_URL}, subject: "${JOB_NAME} build# ${BUILD_NUMBER} FAILED" , to: 'mahrukh.anwari@xflowresearch.com'
		}
		
		
	}
}
