pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'echo "in pipeline"'
      }
    }

    stage('deploy') {
      steps {
        echo 'in deployment'
      }
    }

    stage('post') {
      steps {
        echo 'success'
      }
    }

  }
}