# -*- codeing = utf-8


import unittest

from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import TestAddgoodsask


class TestDbApiAddGoodsAsk(unittest.TestCase):

    def setUp(self) -> None:

        self.mylog = MyLog.get_log()

    def test_api_addgoodsask(self):

        url,data,method,expected = TestAddgoodsask.urls[0],TestAddgoodsask.datas[0],TestAddgoodsask.methods[0],TestAddgoodsask.expecteds[0]

        res = ConfigHttp(url=url,data=data,method=method).request().json()

        self.mylog.debug("----test_api_addgoodsask----，响应结果{}".format(res))

        self.assertEqual(["添加商品咨询成功!"],expected)