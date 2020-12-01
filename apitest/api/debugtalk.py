# -*- codeing = utf-8
from apitest.common.configHttp import ConfigHttp
from apitest.params.params import TestApijobLogin, TestApijobLogout
from apitest.params.params import TestApiLogin, TestApiLogout


def dbshop_login(user_name, user_password, user_unionid):
    # given
    url, data, method = TestApiLogin.urls[0], TestApiLogin.datas[0], TestApiLogin.methods[0],

    data.update(
        {
            'user_name': user_name,
            'user_password': user_password,
            'user_unionid': user_unionid
        }
    )
    # when
    return  ConfigHttp(url=url, data=data, method=method).request().json()

def dbshop_logout(token):
    url, method = TestApiLogout.urls[0], TestApiLogout.methods[0]

    data = {
        "user_token": token
    }

    return ConfigHttp(url=url, data=data, method=method).request().json()
