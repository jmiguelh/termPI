
import firebase_admin 
from firebase_admin import credentials

cred = credentials.Certificate('termpi-firebase-adminsdk-mfrvk-b95cdce7ef.json')
firebase_admin.initialize_app(cred)
