# -*- codeing = utf-8

import unittest

from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import TestApigoodsClass
import re


class TestDbApiGoodsclass(unittest.TestCase):

    def setUp(self) -> None:
        self.mylog = MyLog.get_log()

    def test_db_api_goodsClass(self):
        '''
        商品分类
        :return:
        '''
        url,data,method =TestApigoodsClass.urls[0],TestApigoodsClass.datas[0],TestApigoodsClass.methods[0]

        res = ConfigHttp(url=url,params=data,method=method).request()

        self.mylog.debug("----test_db_api_goodsClass---,响应结果为{}".format(res))

        pattern = re.compile(r"\"class_name\":\"(.+?)\"")

        class_name_list = pattern.findall(res.text)

        self.assertListEqual(class_name_list,['家用电器'])
        #断言失败，该用例未通过，存在bug

    def tearDown(self) -> None:

        pass
