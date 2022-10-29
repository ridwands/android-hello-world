
pipeline {
    agent {
        docker { image 'ridwands/android-sdk' }
    }
    environment { 
            WEBHOOK_SLACK_NOTIFICATION_ANDROID = credentials('WEBHOOK_SLACK_NOTIFICATION_ANDROID') 
        }
    stages {
        stage("Build App"){
            steps{
                sh './gradlew assemble'
            }
        }
        stage("Artifacts"){
            steps{
                archiveArtifacts artifacts: 'app/build/outputs/apk/'
            }
        }
    }
    post { 
        cleanup { 
          cleanWs()
        }
        success{
            sh "python3 iaac/notification-success.py"
        }
    }
}

