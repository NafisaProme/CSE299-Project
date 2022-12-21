import json
import requests
from datetime import datetime

#drive api authorization
def upload_to_drive():
    headers = {"Authorization": "Bearer ya29.a0AX9GBdWX7VoODy5l9gs_4sFIjQQRLJ1Ymg0gDyu7M7MhHAynwkhOB7Q6sQzqlRlPceg28EHJ3VEIvWiD04H7-bdWkE2pGuAJ7moutP8bmok2HuMNn3wX2cya9SEv6Uue7kzLs0kIXeyhVibXMONZzQ43Kl-0aCgYKARUSARMSFQHUCsbCHtbqy3ihfb-yR5bwvmsetA0163"}
    para = {
        "name": str(datetime.today().strftime("%d/%m/%Y")) + " " + str(datetime.now().strftime("%H:%M:%S")),
        "parents":["1yJiFzXpGRCYKsQZp3K8BS4LKPWnHvSOh"]
    }
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'), 'file': open("backend\\attendance.csv", "rb")
    }
    #post request
    r = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files
    )
    print(r.text)