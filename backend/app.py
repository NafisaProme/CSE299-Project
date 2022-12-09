import json
import requests
from datetime import datetime

def work():
    headers = {"Authorization":"Bearer ya29.a0AeTM1idzzs03nak2EopUq15cJgyTaJd0nzKnE4Nj27aQnEIFuodCDeqUjMsCuPz3g-KT_IOzTrqPvSyFLW21-Gd8ahrMMekxZfIehYcJbIu3rjU-3sCeWaWFpqCg0ypKemYpsmT1snN8rBl7htB-k5iRtvtraCgYKAbISARESFQHWtWOm2qasiaPnarDFWR6rO61avw0163"}
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