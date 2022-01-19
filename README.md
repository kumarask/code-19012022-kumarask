# Code Test App

This app has written in flask and reactJs. It is a simple app.

# Prerequisite

Install follow tools using below commands on ubuntu OS.

* sudo apt install make
* sudo apt install python3.8-venv
* sudo apt install npm
* sudo npm install n -g
* sudo n stable
* sudo install semver
* sudo npm install -g npm@8.3.1

# Usage

* clone this project using below command.\
    `git clone git@github.com:kumarask/code-19012022-kumarask.git`
* Navigate into the project folder.\
    `cd code-19012022-kumarask`
* Run `make build` it creates the virtual environment and install the app.
* Run `make run` command to host the server in the machine.
* Launch firefox and type url (`http://localhost:5000`)
* Fill the team name and role name input box, example team name is DevOpsTeam and role name is DevOpsEnggineer.
* Click on Update button. it will create a new records and store it in a database.
* Click on url search bar and type the url (`http://localhost:5000/getRoleNamesByTeamName?teamName=DevOpsTeam`)
* Run `make clean` command In case if you want to clean the environment. 


# Using CURL command
* launch new terminal and execute below url to fetch data.
    `curl -X GET http://localhost:5000/getData`

# API Document
http://localhost:5000/swagger
