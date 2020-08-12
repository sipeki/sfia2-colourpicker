# Colour Picker

Projected started on the 21st of July 2020
Development completed 6th of August 2020

Simon Kindlen, DevOps and Cloud Consultant, QA

![Simon kindlen](https://i.imgur.com/DAaZve5.jpg)

Introduction

> Introduction: In the next 20 to 25 minutes you will be taken through my project for SFIA2. Demonstrating the technologies learnt in the last 3 weeks on developing an application based on micro services architecture.  

>Resources
>Asana Storyboard: https://app.asana.com/share/kindlen/sfia2-colour-picker/1186329697660093/a8fb033118f395ec2face3a1e5db5949

# Contents

* Project Brief
  * Requirements
  * Technologies
* Project Proposal
  * Overview of the Application
  * MoSCoW User Stories & Sprints
  * Services
  * Wireframe
  * Logic
  * ERD
* Project Tracking
* Deployment
  * CI Pipeline and DevOps Tools
  * Jenkins Pipline
  * GitHUB Feature Branch Log
* Risk Assessment
* Best Practices & Security
* Future Implementation
* Retrospective

------

# Project Brief

## Requirements

* An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
* An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine instance.
* Webhooks should be used for Jenkins to automatically recreate and redeploy micro services when changes made to the code base
* Service-oriented architecture rather than monolithic design
* Containerisation and orchestration for micro services deployment
* Ansible Playbook that will provision the environment that your application needs to run.

## The Technologies Stack

* Asana: Kanban Board
* Github: Version Control
* Jenkins: CI Server
* Ansible Playbook: Provision of application environment
* GCP: Virtual machine and database
* Docker: Containerisation:
* Docker Swarm: Orchestration Tool
* NGINX: Reverse proxy and load balancing
* IDE: Microsoft Visual Studio

# Project Proposal

## Overview of the Application

![Colour Picker](https://i.imgur.com/Cx9idt4.jpg) 

Colour Picker. Press button to  generate colour and synonym combination for a descriptive colour.
Colour chosen randomly from either list of basic primary or secondary colours. Synonym chosen randomly from a list of negative or positive synonyms.

## MoSCoW User Stories & Sprints

Moscow prioritisation for project prioritization for functionality.

### Must Sprint

Initial functionality of the application is to show the current generated colour

### Should Sprint

Record colours generated presistantly

### Could Sprint

Reverse Proxy NGINX

Ansible to deploy environment

### Will not

Generate colour from a table from a database rather than hard code into application.

### Micro Services

### Service 1

Renders single html dynamic webpage through Flask. On button pressed communicates through an API to service 4 for colour picked. Inserts value into a database and displays on web page.

### Service 2 Colour

Random selection of colour from either Basic or Secondary list

Basic colours
Red, Yellow, Blue, Yellow, White, Balck

Secondary colours
Indigo, Magenta, Pink, Brown, Gray, Orange, Green, Violet, Purple, Silver, Gold, Platinum

### Service 3  Synonyms

Random selection of synonm from either Positive or Negative list

Words that Embrace Color:
Ablaze, Beaming, Bold, Bright, Brilliant, Colorful, Dappled, Deep - Dark, Delicate, Electric, Festive, Fiery, Flamboyant, Flaming, Fresh, Glistening, Glittering, Glowing, Harmonious, Iridescent, Jazzy, Opalescent, Prismatic, Radiant, Sepia, Vibrant, Vivid

OR

Color Words with Negative Connotations:
Ashy, Bleak, Blotchy, Brash, Chintzy, Cold, Colorless, Dark, Dim, Discolored, Drab, Harsh, Loud, Muddy, Opaque, Saturated, Showy, Sickly, Somber, Sooty, Splashy, Stained, Uneven, Washed-out, Watery

### Service 4

Through API communicates to Service 2 random colour and Service 3 random synonym for generated text.

## Wireframe

### Colour Picker Sprint 1

![Colour Picker Sprint 1](https://i.imgur.com/EipLQlE.png)

### Colour Picker Sprint 3

![Colour Picker Sprint 3](https://i.imgur.com/qdZirSD.png)

## Logic

![Colour Picker process](https://i.imgur.com/IW8DFxN.png)

## ERD

Table for storing presistely colours generated.

![Colour Picker table](https://i.imgur.com/YWsAfN5.png)

## Project Tracking

Asana board used for tracking the project and organise the sprints

https://app.asana.com/share/kindlen/sfia2-colour-picker/1186329697660093/a8fb033118f395ec2face3a1e5db5949

### Start

![Project Tracking Start](https://i.imgur.com/gMsZNbw.jpg)

### During Sprint

![Project Tracking During Sprint](https://i.imgur.com/SNgA2kJ.jpg)

### End of current development cycle
![Project Racking end ](https://i.imgur.com/upZlzuH.jpg)

# Deployment 

## CI Pipeline and DevOps Tools

![CI Pipeline](https://i.imgur.com/Eic4LHU.png)

* Micro Services architecture makes full use of the CI. The automated deployment of service updates to the environment is initiated by a source code update to the GitHib repository. Webhook initiates the Jenkins Pipeline. 

* At first an alternative method was implemented for deployment of the Docker Swarm on how the images were built. That was to have Docker Hub create the images for the micro services and the Jenkins to pull those images to deploy Docker Swarm. The issue with this approach is that the building of images is not instant. Once a commit has been pushed to GitHub Jenkins would start a time to wait 10 minutes. It is not certain that a Docker hub would do the build of the image within 10 minutes. Even if time was not an issue uncertainty in a computing environment runs a higher risk of failure of the pipeline. The changes pushed to the Git repository managed by Github that automatically propagates to Jenkins using webhook is a robust and better method.

## Jenkins Pipeline

![Jenkins Pipeline](https://i.imgur.com/Rf3V0yd.png)

* The deploy process is automated but requires DevOps configuration when it comes to security. Current understanding requires a manual Docker Login to authenticate Docker Swarm manager to Docker Hub when the manager is initially setup. Otherwise permission denied when pushing images to Docker Hub will cause Jenkins run to fail. SSH logon on from Docker Swarm Manager host to Docker Swarm is also required for initial configuration to be set for when Ansible carried out a SSH to join VM instance to Docker Swarm as a Worker. SSh needs to be setup for Jenkins user as well.

![Jenkins Pipeline webpage ](https://i.imgur.com/Kq3SsWa.jpg)

# GITHUB Feature Branch Log

![GITHUB Feature Branch Log](https://i.imgur.com/FBM0pnE.jpg)

# Risk Assessment

![Risk assessment](https://i.imgur.com/TYOpR9c.jpg)

# Best Practices & Security

* Due to the public nature of Github it is important not to upload public ip addresses, database connection details and ports. 
* No unique variables used to access the VM and SQL instances  set in the OS environment.
* Hide ports by configure NGINX to port forward to the API host ports
* Host ip addresses set in Hosts file for Docker Swarm Worker
* Manually test all stages in Jenkins by running the pipeline stages as Jenkins user from Docker Swarm Manager the terminal
* Test and compile a list of required packages to be installed for the micros services at each sprint epoch epic by running the services locally from the terminal by creating a virtual environment with Python Venv. 
* To stop cached files be pushed to github and docker hub create .gitignore and .dockerignore 

# Future Implementation

* Database for table of synonyms and colours. Enabling users to add their own colour and synonyms.
* Record user name and mood they are in at that moment. The mood will set what type of synonym to combine with colour.
* Visualize the colour generated.
* Skin the website to be more visually appealing.
* Only update the micro service that's source code has been modified rather than all micro services when a weebhook is detected.
* Run the database for persistent data as a part of the Docker Swarm.

# Retrospective

* When everything is as it should be and the micro service still does not run means that there is a fundamental issue with the declarations before the function is declared.
* Solo work is a slower process rather than in groups.
* A secure implementation requires DevOps to carry out manual tasks. SSH Docker Login is an example.
* Containerization provides a flexible method to roll out micro services without overhead of setting up box. It is elastic.
* Right at the start it was difficult to visualise in my head how the application was to be developed as I technologies frameworks and concepts were unknown.
* Devops, cloud computing, containerisation, micro services are perfect symbiosis.
* Containers are immutable. No longer have to provide root access to the box reduced attack surface with less vectors.

> Author: Simon Kindlen
