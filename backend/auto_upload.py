import schedule
import time 
from app import *

def run_app():
    work()

schedule.every(5).seconds.do(run_app)

while 1:
    schedule.run_pending()
    time.sleep(1)
