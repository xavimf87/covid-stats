pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        echo 'Probando en modo Test'
      }
    }

    stage('Install Pip Packages') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }

  }
}