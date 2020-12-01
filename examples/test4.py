# -*- codeing = utf-8
import requests
import re

url = "http://116.85.42.10/Jsonapi/goodsInfo?apikey=df1ecd59ab26d0a46ac39f0a5cf92dc1"

payload='goods_id=10&class_id=31&user_token=160ad0b9e99324d1f381a02db7184c63'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'PHPSESSID=qr9ea7b4j554rv96qv88u4cs43'
}

response = requests.request("POST", url, headers=headers, data=payload)

pattern = re.compile(r"\"goods_name\":\"(.+?)\"")

match = pattern.findall(response.text)

print(match)


