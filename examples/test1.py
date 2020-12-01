# -*- codeing = utf-8
import pprint
import re
import requests

url = "http://116.85.42.10/Jsonapi/specialCms?cms_code=example0&apikey=df1ecd59ab26d0a46ac39f0a5cf92dc1"

payload={}
headers = {
  'Cookie': 'PHPSESSID=cgofiohvm1ms8rno4tk5r6ag92'
}

response = requests.request("GET", url, headers=headers, data=payload)

content = response.text

# print(content)

pattern = re.compile(r"\"single_article_title\":\"(.+?)\"")
#
match = pattern.findall(content) # 列表

print(match)
