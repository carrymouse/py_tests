# -*- codeing = utf-8



from apitest.api.debugtalk import dbshop_login

login_res = dbshop_login("test1","123456",1)

print(login_res)

token = login_res["result"]["user_token"]
print(token)