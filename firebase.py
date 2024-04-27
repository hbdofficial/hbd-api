# This contains all the configuration reated to firebase

import firebase_admin
from firebase_admin import credentials, storage

from config import FIREBASE_CONFIG

cred = credentials.Certificate(FIREBASE_CONFIG)
firebase_admin.initialize_app(cred, {
	'storageBucket':'hbd-backend.appspot.com'
})

# Getting the firebase storage service
bucket = storage.bucket()