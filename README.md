# Colour Picker

Projected started on the 21st of July 2020
Development completed 6th of August 2020

Simon Kindlen, DevOps and Cloud Consultant, QA

![Simon kindlen](https://i.imgur.com/DAaZve5.jpg)


Introduction

>Introduction: In the next 10 to minutes you will be taken through my project for SFIA2. Demonstrating the technologies learnt in the last 3 weeks on developing an application based on micro services architecture.  



### Resources


Asana Storyboard: https://app.asana.com/share/kindlen/sfia2-colour-picker/1186329697660093/a8fb033118f395ec2face3a1e5db5949


# Content

* Project Brief
    * Requirements
    * Technologies
    * Overview

* Story Board
* Risk Assessment
* Project Proposal
* Application
    * Process
    * ERD
* Deployment
* Security
* Improvements

------

# Project Brief

## Requirements

* An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
* An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a * CI server and deployed to a cloud-based virtual machine.
* Webhooks should be used for Jenkins to automatically recreate and redeploy micro services when changes made to the code base
* Service-oriented architecture rather than monolithic design
* Containerisation and orchestration for micro services deployment
* Ansible Playbook that will provision the environment that your application needs to run.

## The Technologies Stack
* Asana: Kanban Board
* Git: Version Control
* Jenkins: CI Server 
* Ansible Playbook: Provision of application environment
* GCP: Virtual machine and database
* Docker: Containerisation:
* Docker Swarm: Orchestration Tool: 
* NGINX: Reverse proxy and load balancing

Project Proposal

## Overview of the Application

![Colour Picker](https://i.imgur.com/Cx9idt4.jpg) 
Colour Picker. Press button to  generate colour and synonym combination for a descriptive colour.
Colour chosen randomly from either list of basic primary or secondary colours. Synonym chosen randomly from a list of negative or positive synonyms.


### Services 

#### Service 1 
Renders single html dynamic webpage through Flask. On button pressed communicates through an API to service 4 for colour picked.Inserts value into a database and displays on web page.


#### Service 2 Colour
Basic colours
Red, Yellow, Blue, Yellow, White, Balck

Secondary colours
Indigo, Magenta, Pink, Brown, Gray, Orange, Green, Violet, Purple, Silver, Gold, Platinum

#### Service 3  Synonyms

Words that Embrace Color:
Ablaze, Beaming, Bold, Bright, Brilliant, Colorful, Dappled, Deep - Dark, Delicate, Electric, Festive, Fiery, Flamboyant, Flaming, Fresh, Glistening, Glittering, Glowing, Harmonious, Iridescent, Jazzy, Opalescent, Prismatic, Radiant, Sepia, Vibrant, Vivid

OR

Color Words with Negative Connotations:
Ashy, Bleak, Blotchy, Brash, Chintzy, Cold, Colorless, Dark, Dim, Discolored, Drab, Harsh, Loud, Muddy, Opaque, Saturated, Showy, Sickly, Somber, Sooty, Splashy, Stained, Uneven, Washed-out, Watery

#### Service 4
Through API communicates to Service 2 for colour and Service 3 for generated text.


### Process design 

![Colour Picker process](https://i.imgur.com/IW8DFxN.png)


### ERD
Table for storing presistely colours generated

![Colour Picker table](https://i.imgur.com/QU4xmuE.jpg)


### MoSCoW
Moscow prioritisation used required CRUD functionality

#### Must
Initial functionality of the application is to show the current generated colour

#### Should
Record colours generated presistantly


#### Could
Reverse Proxy
Ansible to deploy environment

#### Will not
Generate colour from a table from a database rather than hard code into application.

