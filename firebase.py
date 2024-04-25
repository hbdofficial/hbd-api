# This contains all the configuration reated to firebase

import json
import pyrebase

from config import FIREBASE_CONFIG

#config for the firebase
config = {
	"apiKey": "AIzaSyDeUM5Zx3ppESKtAIAYlWsRXSa_zcXIwag",
	"authDomain": "hbd-backend.firebaseapp.com",
	"storageBucket":"hbd-backend.appspot.com",
	"databaseURL":""
}

firebase = pyrebase.initialize_app(config)

# Getting the firebase storage service
storage = firebase.storage()