# HBD API
This is the repository for the HBD API. This API is used across mobile and web apps of the HBD.

## How to get started 

This project has been built using *python 3.12*

### Prerequisities

1. Need to initialize a python environment
   ```shell
   python -m venv /path/to/the/folder
	```
2. Navigate to the folder
	```shell
	cd /path/to/the/folder
	```
3. Activate the virtual environment
	1. Unix like environments
	```shell
	source ./bin/activate
	```
	2. For Windows
		1. Using powershell
		```shell
		.\Scripts\Activate.ps1
		```
		2. Using command prompt
		```shell
		.\Scripts\activate.bat
		```

*It is assumed that the virtual environment is activated to follow the below steps*

### Cloning and installing packages

1. Clone the repo in to the virtual environment.
   ```shell
   git clone git@github.com:hbdofficial/hbd-api.git app
   ```
   Never change the folder name *app* anything else.
2. Install all the packages using the command.
   ```shell
   pip install -r requirements.txt
   ```
3. Set DATABASE_URL in .env file.
   Make sure a requirements.txt file is in the repo. Otherwise report it to the HBD authority.

### Generate the Database

You need to have a local or cloud hosted postgres database in order to run the API.

1. Set the database url to DATABASE_URL in .env
2. Run the following commands to migrate models.
   ```shell
   alembic revision --autogenerate -m "Initial Generation"
   ```
3. Apply the migrations to the database
   ```shell
	alembic upgrade head
   ```