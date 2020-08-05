pipeline {

    agent any

    stages {

        stage("Start NGINX") {

            steps {

                sh './scripts/startnginx.sh'

            }

        }
        
        // stage("Build Swarm") {

        //     steps {
                
                
        //         sh './scripts/ansible.sh'

        //     }

        // }
        
        stage("Build Images") {

            steps {
                sh 'chmod +x ./scripts/*.sh'
                sh './scripts/build_images.sh'

            }

        }

        stage("Deploy Stack") {

            steps {

                sh './scripts/deploy_stack.sh'

            }
        } 

        stage("Update Service") {

            steps {

                sh './scripts/update_services.sh'

            }
        }

        stage("Clean Up Services Images Containers") {

            steps {

                sh './scripts/clean_up.sh'

            }
        }

    }




}