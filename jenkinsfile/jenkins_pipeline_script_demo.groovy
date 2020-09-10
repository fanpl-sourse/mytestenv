pipeline {
    agent any

    stages {
        stage('begin') {
            steps {
                echo 'Hello World'
            }
        }
    }
    post {
          always{
          echo 'hi fanpl'
          }
    }
}