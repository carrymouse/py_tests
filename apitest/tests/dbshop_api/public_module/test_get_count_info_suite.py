# -*- codeing = utf-8

import unittest

from ddt import file_data, ddt

from apitest.api.debugtalk import dbshop_login, dbshop_logout
from apitest.common.configHttp import ConfigHttp
from apitest.params.params import TestApiStatistics


@ddt
class TestGetCountInfoSuite(unittest.TestCase):

    @file_data(r"D:\cs_apitest\cs_apitest\apitest\data\test_get_count_info_data.json")
    def test_api_statistics(self, user_name, user_password, user_unionid):

        res = dbshop_login( user_name, user_password, user_unionid)

        # out
        global token
        token = res["result"]["user_token"]
        #
        url, data, method = TestApiStatistics.urls[1], TestApiStatistics.datas[1], TestApiStatistics.methods[1]

        data.update(
            {
                "user_token": token
            }
        )
        # when
        res = ConfigHttp(url=url, data=data, method=method).request().json()

        self.assertEqual(6, res["result"][0]["favorites_num"], " 失败")

        # 退出

    def tearDown(self) -> None:
        global  token
        res = dbshop_logout(token)
        self.assertEqual("success", res["status"], "退出失败")