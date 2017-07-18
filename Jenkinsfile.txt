Jenkinsfile (Declarative Pipeline)
#this is just a line that is added it does not serve any purpose 
pipeline {
    agent { docker 'python:3.5.1' }
    stages {
        stage('build') {
            steps {
		python './pytest.py'
            }
        }
    }
}