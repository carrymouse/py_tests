# -*- codeing = utf-8

import unittest

from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import TestConnCase


class TestConn(unittest.TestCase):

    def setUp(self) -> None:
        self.log = MyLog.get_log()

    def test_1(self):

        method =  TestConnCase.methods[0]

        content =  ConfigHttp(method=method,url="").request().json()

        self.log.debug("连接响应数据 ==={}".format(content))

        self.assertEqual("success", content["status"],"连接测试不通过")

    def test_2(self):
        pass

