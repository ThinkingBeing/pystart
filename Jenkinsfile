pipeline {
  agent none
  stages {
    stage('cd') {
      steps {
        powershell(script: 'cd c:/dev/src/pystart', returnStatus: true, returnStdout: true)
      }
    }
  }
}