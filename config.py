# This contains all the backend configuration

import os
import json

# Using dotenv for loading envs
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = str(os.getenv("DATABASE_URL"))
FIREBASE_CONFIG = json.loads(str(os.getenv("FIREBASE_CONFIG")))