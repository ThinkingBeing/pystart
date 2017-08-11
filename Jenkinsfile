pipeline {
  agent {
    node {
      label 'master'
    }
    
  }
  stages {
    stage('cd') {
      steps {
        powershell(script: 'cd c:/dev/src/pystart', returnStatus: true, returnStdout: true)
      }
    }
  }
}