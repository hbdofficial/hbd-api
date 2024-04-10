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
	
	```

1. Clone the repo in the virtual environment
2. Set DATABASE_URL in .env file.
3. Install all the packages using the command
   ```shell
   pip install requirements.txt
   ```
   Make sure a requirements.txt file is in the repo. Otherwise report it to the HBD authority.
4. If *alembic* folder is not present. Run the follwing commands.
	```shell
	cd folder_where_repo_is_located/app 
	alembic init 
	```