# Code Test App

This app has written in flask and reactJs. It is a simple app.

# Usage

* clone this project using below command.\
    ``
* Navigate into the project folder.\
    `cd code-19012022-kumarask`
* Run `make build` it creates the virtual environment and install the app.
* Run `make run` command to host the server in the machine.
* Launch firefox and type url (`http://localhost:5000`)
* Fill the team name and role name input box, example team name is DevOpsTeam and role name is DevOpsEnggineer.
* Click on Update button. it will create a new records and store it in a database.
* Click on url search bar and type the url (`http://localhost:5000/getRoleByTeamName?teamName=DevOpsTeam`)
* Run `make clean` command In case if you want to clean the environment. 


# Using CURL command
* launch new terminal and execute below url to fetch data.
    `curl -X GET http://localhost:5000/getData`