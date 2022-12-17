import firebase_admin
from firebase_admin import credentials, storage
from google.cloud import storage
from google.oauth2 import service_account

# connecting to the firebase storage
cred = credentials.Certificate("backend\\attendancecamera-15e2e843f42e.json")
firebase_admin.initialize_app(cred, {'storageBucket': 'attendancecamera.appspot.com'})

def import_image():
    # downloading an image from firebase stoSbrage
    credential = service_account.Credentials.from_service_account_file("backend\\attendancecamera-15e2e843f42e.json")
    storage.Client(credentials=credential).bucket(firebase_admin.storage.bucket().name).blob('1').download_to_filename('backend/test_image/Test.jpg')