import firebase_admin
from firebase_admin import credentials, storage
from google.cloud import storage
from google.oauth2 import service_account

# connecting to the firebase storage 
cred = credentials.Certificate("backend\\attendancecamera-15e2e843f42e.json")
firebase_admin.initialize_app(cred,{'storageBucket': 'attendancecamera.appspot.com'})

# uploading a local file to the firebase server 
# file_path = "backend\\resources\\test_image.png"
# bucket = storage.bucket()  # storage bucket
# blob = bucket.blob(file_path)
# blob.upload_from_filename(file_path)

# downloading an image from firebase storage 
credentials = service_account.Credentials.from_service_account_file("backend\\attendancecamera-15e2e843f42e.json")
storage.Client(credentials=credentials).bucket(firebase_admin.storage.bucket().name).blob('Screenshot (786).png').download_to_filename('backend/resources/Test.png')

files = storage.Client(credentials=credentials).list_blobs(firebase_admin.storage.bucket().name)
for i in files: print('The public url is ', i.public_url)
