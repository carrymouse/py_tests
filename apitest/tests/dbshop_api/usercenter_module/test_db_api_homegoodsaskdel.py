# -*- codeing = utf-8

import unittest

from apitest.api.debugtalk import dbshop_login
from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import TestApihomeGoodsAskDel, TestApiLogin


class TestDbApihomeGoodsAskDel(unittest.TestCase):

    def setUp(self) -> None:
        self.mylog = MyLog.get_log()

    def test_api_homegoodsaskdel(self):
        user_name, user_password, user_unionid = TestApiLogin.datas[0]["user_name"],  TestApiLogin.datas[0]["user_password"],TestApiLogin.datas[0]["user_unionid"]

        login_res = dbshop_login(user_name, user_password, user_unionid)

        token = login_res["result"]["user_token"]

        url,data,method,expected = TestApihomeGoodsAskDel.urls[0],TestApihomeGoodsAskDel.datas[0],TestApihomeGoodsAskDel.methods[0],TestApihomeGoodsAskDel.expecteds[0]

        data.update({
            "user_token":token
        })

        res = ConfigHttp(url=url,data=data,method=method).request().json()

        self.mylog.debug("---test_api_homegoodsaskdel---,响应结果为{}".format(res))

        self.assertEqual(res['status'],expected)