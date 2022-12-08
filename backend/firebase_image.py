import firebase_admin
from firebase_admin import credentials, storage
cred = credentials.Certificate("backend\\attendancecamera-15e2e843f42e.json")
firebase_admin.initialize_app(cred,{'storageBucket': 'attendancecamera.appspot.com'})

file_path = "backend\\resources\\test_image.png"
bucket = storage.bucket()  # storage bucket
blob = bucket.blob(file_path)
blob.upload_from_filename(file_path)