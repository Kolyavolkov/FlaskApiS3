properties([disableConcurrentBuilds()])

def VERSION = sh (script: """git log --format="medium" -1 ${GIT_COMMIT}""", returnStdout:true) 
def TAG = "kolyavolkov/restapi3:${VERSION}"

pipeline {
    agent {
        label 'master'
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '5', artifactNumToKeepStr: '5'))
        timestamps()
    }
    environment {
		DOCKERHUB_CREDENTIALS=credentials('kolyavolkov')
	}
    stages {
        stage("build docker image") {
            steps {
                echo "======== building image ========"
                sh "docker build  -t ${TAG} ./project"
                
            }
        stage("push docker image") {
            echo "======== pushing image to dockerhub ========"
                sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
                sh "docker push ${TAG}"
        }    

        }
    }
}