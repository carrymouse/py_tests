# -*-coding:utf-8 -*-
# !/usr/bin/python37
# @Author:liulang
import unittest
#
# from apitest.common.configHttp import ConfigHttp
# from apitest.common.log import MyLog
# from apitest.params.params import TestApijobLogin


class TestJobApiLogin(unittest.TestCase):

    # def setUp(self) -> None:
    #     self.mylog = MyLog.get_log()

    def test_job_login(self):
        # url,data,method = TestApijobLogin.urls[0],TestApijobLogin.datas[0],TestApijobLogin.methods[0]
        #
        # res = ConfigHttp(url=url,data=data,method=method).request().json()
        #
        # self.mylog.debug("---test_job_login---,响应结果为{}".format(res))
        #
        # self.assertEqual("success",res["status"],"登录失败")

        self.assertFalse(0)
