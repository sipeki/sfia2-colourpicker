pipeline {

    agent any

    stages {

        stage("Pull Images") {

            steps {

             
                sh 'chmod +x ./scripts/*.sh'
                sh './scripts/pull_images.sh'

            }

        }

        stage("Build Services") {

            steps {

                sh './scripts/build_build.sh'

            }
        
        stage("Update Services") {

            steps {

                sh './scripts/swarm_setup.sh'
                sh './scripts/build_services.sh'

            }


        


    }




}