import schedule
import time 
from DriveUploader import *
from FirebaseRetriever import *
from MarkAttendance import *

<<<<<<< HEAD
# function which would import the image, mark the attendance and upload csv file to drive
=======
#calling the function
>>>>>>> 9dc9865366b9393cb14c94566de330e6fbc9487b
def run_app():
    import_image()
    attendance()
    upload_to_drive()

<<<<<<< HEAD
# the above function would run every 10 seconds 
=======
#scheduling the function to run automatically
>>>>>>> 9dc9865366b9393cb14c94566de330e6fbc9487b
schedule.every(10).seconds.do(run_app)

while 1:
    schedule.run_pending()
    time.sleep(1)
