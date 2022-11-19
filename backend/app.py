import json
import requests
from datetime import date

headers = {"Authorization":"Bearer ya29.a0AeTM1icZmKHTSlssq1y9IuWDU1Qxi4ELjpdYisgDxB34FE7wxwPcvMGKFERUcXwgBirYzTxo-4jFXHrjyjtTRBekQWyBXvt6HtziQl2hGQUqfuYUwL_y9jL6hTRASN0JX0fYX9Ibpwx_e8mlfhPHvi6tjvMHaCgYKAe0SARESFQHWtWOmI4eriWMu7URGExZMaMEM_Q0163"}
para = {
    "name": str(date.today().strftime("%d/%m/%Y")),
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