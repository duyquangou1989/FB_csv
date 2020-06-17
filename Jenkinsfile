pipeline {
	agent any

	stages {
		stage('Build') {
			steps {
				echo 'Build ... '
				cat test.txt
			}
		}

		stage('Test') {
			steps {
				echo 'Testing ... '
			}
		}
		
		stage('Deploy') {
			steps {
				echo 'Deploying ...'
			}
		}
	}

}
