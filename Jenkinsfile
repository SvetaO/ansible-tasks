pipeline {
    agent {
        dockerfile true 
    }
    stages {
        stage('Build docker image & run python script') {
            steps {
                echo "Hello from simple script"
                sh "python ./simple.py"
            }
        }
    }
}