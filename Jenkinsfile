pipeline {
  agent any
  stages {
    stage('pull') {
      steps {
        echo 'start pull'
        powershell(script: 'cd c:/dev/src/pystart', returnStatus: true)
        powershell(script: 'git pull', returnStdout: true)
      }
    }
    stage('test') {
      steps {
        powershell(script: 'python setup.py test', returnStdout: true)
      }
    }
  }
}