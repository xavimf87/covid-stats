pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        echo 'Probando en modo Test'
      }
    }

    stage('Git clone') {
      agent {
        dockerfile {
          filename 'docker-compose.yml'
        }

      }
      steps {
        git(url: 'https://github.com/xavimf87/covid-stats.git', branch: 'master')
      }
    }

  }
}