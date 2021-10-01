properties([disableConcurrentBuilds()])

def REPO = "kolyavolkov/restapi3"

pipeline {
    agent {
        label 'master'
    }
    environment {
        tag = sh(returnStdout: true, script: "git rev-parse --short=10 HEAD").trim()
        DOCKERHUB_CREDENTIALS=credentials('kolyavolkov')
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '5', artifactNumToKeepStr: '5'))
        timestamps()
    }
    stages {
        stage("build docker image") {
            steps {
                echo "======== building image ========"
                sh "docker build -f Dockerfile -t ${REPO}:${tag} ./project"
            }
        }
        stage("push docker image") {
            steps {
                echo "======== pushing image to dockerhub ========"
                sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
                sh "docker push ${REPO}:${tag}"
            }
        }    
        }
    }
