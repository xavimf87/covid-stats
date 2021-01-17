pipeline {
    environment {
        BRANCH_NAME = "${GIT_BRANCH.split("/")[1]}"
    }
    agent any

    stages {
        stage('Build') {
            steps {
                echo "Building...${ACTUAL_BRANCH}"  
                sh "pip3 install -r requirements.txt"
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                echo 'python3 run.py'

            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
        stage('Destroy') {
            steps {
                echo 'Destroy....'
            }
        }
    }
}