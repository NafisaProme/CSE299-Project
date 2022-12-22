import json
import requests
from datetime import datetime

#drive api authorization
def upload_to_drive():
    # google playground api 
    headers = {"Authorization": "Bearer ya29.a0AX9GBdUP9rGZFLo6ogF2rrqmkZAIMTJjV5t1oh-elntsNQwajY3DFP9qqyaAO-IuqHFiNVdSxPRPAk4Ox30sP4MqyCI5R0FjgJiK-yi4lr4QM-Rfzu2mRY22R2ybpcMmuxCZgTrobaOiWvkFyDBPkjmryzf5aCgYKAQkSARMSFQHUCsbC43_78UYEOT_-GztQ-sqnyg0163"}
    para = {
        "name": str(datetime.today().strftime("%d/%m/%Y")) + " " + str(datetime.now().strftime("%H:%M:%S")),
        "parents":["1yJiFzXpGRCYKsQZp3K8BS4LKPWnHvSOh"]
    }
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'), 'file': open("backend\\attendance.csv", "rb")
    }
<<<<<<< HEAD
    # posting the csv file to google drive 
=======
    #post request
>>>>>>> 9dc9865366b9393cb14c94566de330e6fbc9487b
    r = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files
    )
    print(r.text)