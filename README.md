[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

# Project Title:  CLI-based CRUD
Using a command-line interface, you'll be able to create and delete projects, log the time spent on tasks, and view a summary of the total hours dedicated to each project.


The final application will behave like this:
```sh
    $ dev-time create-project "Project 1"
    $ dev-time create-project "Project 2"
    $ dev-time log-time "Project 1" "2h"
    OK! Logged 120 minutes for Project 1
    $ dev-time log-time "Project 2" "50m"
    OK! Logged 50 minutes for Project 2
    $ dev-time summary
    Total time logged:
    Project 1: 2h
    Project 2: 50min
    $ dev-time delete-project "Project 1"
    $ dev-time snapshot "projects.csv"
    OK! Snapshot saved to projects.csv
```


## Setup
### 1. Install Dependencies:

Ensure Python is installed.


### 2. Install required packages:

``` sh 
$ pip install -r requirements.txt
```
and for developing (tests and contributing), execute
``` sh 
$ pip install -r requirements.txt
```

### 3. Environment Variables:


Create a `.env` file based on the `env.template` file provided in the project.


#### Define the following variables:

- DB_USER=<your_db_user>
- DB_PASSWORD=<your_db_password>
- DB_HOSTNAME=<your_db_hostname>
- DB_SID=<your_db_sid>
- DB_PORT=<your_port>

### Image PostreSQL 
Postre:
``` sh 
    $ docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -e POSTGRES_DB=departements -p 5432:5432 postgres

```

## Execute the script:
Use 
``` sh 
python 
```


## LICENSE: MIT License file.
License
This project is licensed under the MIT License. See the LICENSE file for details.