import schedule
import time 
from DriveUploader import *
from FirebaseRetriever import *
from MarkAttendance import *

#calling the function
def run_app():
    import_image()
    attendance()
    upload_to_drive()

# the above function would run every 10 seconds 
schedule.every(10).seconds.do(run_app)

while 1:
    schedule.run_pending()
    time.sleep(1)
