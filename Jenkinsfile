pipeline {
    agent any
    
    environment {
        props = load 'general.groovy'
	}
    
    options {
        skipStagesAfterUnstable()
    	    }
	    
    stages {
        stage('Build') {
            steps {
                echo "Building from branch"
		            sh 'ls -lrt'
		
			          sh 'ssh ubuntu@ec2-3-19-72-68.us-east-2.compute.amazonaws.com ls -lrt'
			          echo "This is result"
			     }
            }
        }
    
    post {
    	always {
		echo "Wow.... Deleting Zip file from \${WORKSPACE}"
		
		}
	}
}
