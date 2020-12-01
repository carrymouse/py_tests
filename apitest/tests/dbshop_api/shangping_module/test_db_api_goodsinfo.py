# -*- codeing = utf-8

import unittest

from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import TestApigoodsInfo
import re


class TestDbApiGoodsinfo(unittest.TestCase):

    def setUp(self) -> None:

        self.mylog = MyLog.get_log()

    def test_api_goodsinfo(self,):

        url,data,method = TestApigoodsInfo.urls[0],TestApigoodsInfo.datas[0],TestApigoodsInfo.methods[0]

        res = ConfigHttp(url=url,data=data,method=method).request()

        self.mylog.debug("----test_api_goodsinfo----,响应结果为{}".format(res.text))

        pattern = re.compile(r"\"goods_name\":\"(.+?)\"")

        goods_name_list = pattern.findall(res.text)

        self.mylog.debug("----goods_name_list----，响应结果为{}".format(goods_name_list))

        self.assertListEqual(goods_name_list,['皮卡皮卡皮'])

    def tearDown(self) -> None:

        pass