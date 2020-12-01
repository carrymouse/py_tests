# -*- codeing = utf-8

import unittest

from apitest.api.debugtalk import dbshop_login
from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import TestApiStatistics


class TestGetCountInfo(unittest.TestCase):

    def setUp(self) -> None:
        self.dal = TestApiStatistics()
        self.mylog = MyLog.get_log()

    def test_api_login(self):
        data = self.dal.datas[0]
        res = dbshop_login(**data)

        # then
        self.assertEqual("success", res["status"], "登录失败")

        # out
        global token
        token = res["result"]["user_token"]

    def test_api_statistics(self):
        url, data, method = self.dal.urls[1], self.dal.datas[1], self.dal.methods[1]
        global token
        data.update(
            {
                "user_token": token
            }
        )

        # when
        res = ConfigHttp(url=url, data=data, method=method).request().json()

        self.mylog.debug("test_api_statistics---------响应结果{}".format(res))

        self.assertEqual(6, res["result"][0]["favorites_num"], "失败")

    def test_api_logout(self):
        url, method = self.dal.urls[2], self.dal.methods[2]

        res = ConfigHttp(url=url, method=method).request().json()

        self.mylog.debug("test_api_logout---------响应结果{}".format(res))


    def tearDown(self) -> None:
        pass
