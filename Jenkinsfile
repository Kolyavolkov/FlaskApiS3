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
                sh "docker build -f Dockerfile -t ${REPO}:${GIT_COMMIT} -t ${REPO}:latest ./project"
            }
        }
        stage("push docker image") {
            steps {
                withDockerRegistry([ credentialsId: "kolyavolkov", url: "" ]) {
                echo "======== pushing image to dockerhub ========"
                sh "docker push --all-tags ${REPO}"
                }
            }
        stage("clean") {
            steps {
                echo "======== removing images ========"
                sh "docker rmi ${REPO}:${GIT_COMMIT}"
            }
        }    
        }
    }
