import json
import requests
headers = {"Authorization":"Bearer ya29.a0AeTM1ieEYn19Vh4X_UG2kLW-_nICG_7-eOjBfk9YEIkprQbmKwKK1TRe_QXdZs9HAUv5fThBznq4TOhef_8_NeezVzQu1XEsQIrE6puCXCOLJjP7mbyzVlPADayQTA7f4w_y94K9pIY-ONg98qjEZJoBFAEdaCgYKAS0SARESFQHWtWOm6fABSvkvScSrBguKUDpYJw0163"}
para = {
    "name":"Attendance File",
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