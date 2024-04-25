# This contains all the backend configuration

import os

# Using dotenv for loading envs
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = str(os.getenv("DATABASE_URL"))