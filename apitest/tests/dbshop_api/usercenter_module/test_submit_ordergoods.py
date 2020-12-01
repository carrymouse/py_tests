# -*- codeing = utf-8


import unittest

from apitest.api.debugtalk import dbshop_login
from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import TestApiSubmitOrdergoodsComment


class TestSubmitOrdergoods(unittest.TestCase):

    def setUp(self) -> None:

        self.mylog = MyLog.get_log()
        self.dal = TestApiSubmitOrdergoodsComment()

    def test_api_sumbitordergoods(self):

        data = self.dal.datas[0]
        login_res = dbshop_login(**data)

        #global token

        token= login_res["result"]["user_token"]

        url,data,method,expected = self.dal.urls[1],self.dal.datas[1],self.dal.methods[1],self.dal.expecteds[1]

        data.update (
            {
            "user_token": token
        })

        res = ConfigHttp(url=url,data=data,method=method).request().json()

        self.mylog.debug("----提交评价信息------".format(res))

        self.assertEqual("商品评价添加完成!",expected)

    def tearDown(self) -> None:

        pass