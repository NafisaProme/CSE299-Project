import json
import requests
from datetime import datetime

def work():
    headers = {"Authorization":"Bearer ya29.a0AeTM1iepKly0giUY37o2XYmvHTnRDh1342lHx844-Abwp03nEAQ2CMgnXcUiRPes9J1GAK-i8tlLuvUv5cJwxteyEOp0EbK5Yz79Ec7kS7HTAAWNzsQiJFt4hINDz1Fad0ka7o_5UrWZDOcBK_x_sS7Ez5LBaCgYKAQ0SARESFQHWtWOm6aUkyb3R9z5E0B-BFeoEgg0163"}
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