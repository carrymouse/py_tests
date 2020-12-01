# -*- codeing = utf-8

import requests
import re

url = "http://116.85.42.10/Jsonapi/specialGoods?user_token=c2ea760e7c384859a3019bbc335121ec&goods_code=1&apikey=df1ecd59ab26d0a46ac39f0a5cf92dc1"
payload = {}
headers = {
  'Cookie': 'PHPSESSID=cgofiohvm1ms8rno4tk5r6ag92'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

content = response.text

pattern = re.compile(r"\"goods_id\":\"(.+?)\"")

match = pattern.findall(content)
print(match)