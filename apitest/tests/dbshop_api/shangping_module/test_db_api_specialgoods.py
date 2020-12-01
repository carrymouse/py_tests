# -*- codeing = utf-8

import unittest
import re

from apitest.api.debugtalk import dbshop_login
from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import TestApispecialGoods


class TestDbApiSpecialGoods(unittest.TestCase):

    def setUp(self) -> None:
        self.mylog = MyLog.get_log()

        #登录获取token
    def test_get_token(self):

        url,data,method = TestApispecialGoods.urls[0],TestApispecialGoods.datas[0],TestApispecialGoods.methods[0]

        res = ConfigHttp(url=url,data=data, method=method).request().json()

        self.assertEqual("success",res["status"],"登录失败")

        global token
        token = res["result"]["user_token"]

    def test_db_api_specialgoods(self):

        url,data,method =TestApispecialGoods.urls[1],TestApispecialGoods.datas[1],TestApispecialGoods.methods[1]

        global token
        data.update({
            "user_token":token
        })

        res = ConfigHttp(url=url,params=data,method=method).request()

        self.mylog.debug("------test_db_api_specialgoods----,响应结果{}".format(res))

        pattern = re.compile(r"\"goods_id\":\"(.+?)\"")

        goods_id_list = pattern.findall(res.text)

        self.mylog.debug("---goods_id_list-----,响应结果为{}".format(goods_id_list))

        self.assertListEqual(goods_id_list,["7","2"])

    def tearDown(self) -> None:

        pass