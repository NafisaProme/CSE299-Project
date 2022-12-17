import schedule
import time 
from DriveUploader import *
from FirebaseRetriever import *
from MarkAttendance import *

def run_app():
    import_image()
    attendance()
    upload_to_drive()

schedule.every(10).seconds.do(run_app)

while 1:
    schedule.run_pending()
    time.sleep(1)
