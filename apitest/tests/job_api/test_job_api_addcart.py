# -*- codeing = utf-8


import unittest

from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import TestApiaddCart


class TestJobApiAddcart(unittest.TestCase):

    def setUp(self) -> None:
        self.mylog = MyLog.get_log()

    def test_job_api_addCart(self):
        url,data,method = TestApiaddCart.urls[0],TestApiaddCart.datas[0],TestApiaddCart.methods[0]

        res = ConfigHttp(url=url,data=data,method=method).request()

        self.mylog.debug("----test_job_api_addCart---,响应结果为{}".format(res))
