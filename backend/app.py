import json
import requests
from datetime import datetime

def work():
    headers = {"Authorization": "Bearer ya29.a0AeTM1ifh4UU4G9q4NW_Aw1u4YmL3LcVkCWLr6PSU4bJvi5Nq5rxLswrsVin6kS2qYgjyNAogbVkVCtgPJ8XhWEGDo2iMdVfol_TEfUlv5rm0jOWcADGmNHjpf0MO52K-g9xOHx-sc6nx4pPwMO0aW-6Ip5SxaCgYKASYSARMSFQHWtWOm6h3-5fDzLGq7eDtM1bPcVA0163"}
    para = {
        "name": str(datetime.today().strftime("%d/%m/%Y")) + " " + str(datetime.now().strftime("%H:%M:%S")),
        "parents":["1yJiFzXpGRCYKsQZp3K8BS4LKPWnHvSOh"]
    }
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),'file':open("backend/attendance.csv","rb")
    }
    r = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files
    )
    print(r.text)