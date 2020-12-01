# -*- codeing = utf-8
import requests
import re

url = "http://116.85.42.10/Jsonapi/goodsClass?class_id=29&apikey=df1ecd59ab26d0a46ac39f0a5cf92dc1"

payload={}
headers = {
  'Cookie': 'PHPSESSID=jge6ren30j30c7en3pt7ols6l2'
}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)

pattern = re.compile(r"\"class_name\":\"(.+?)\"")

match = pattern.findall(response.text)
print(match)