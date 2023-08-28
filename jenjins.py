    agent any

    stages {
        stage('Hello') {
            steps {
                git 'https://github.com/Surajraikaushik/Abny.git'
                sh  'python Grade.py'
            }
        }
        stage('Success') {
            steps {
                echo 'Welldone!!!!!!!!!!!!'
            }
        }
    }
}
