# -*- codeing = utf-8

import unittest
from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import TestApiSpecialad

class TestApiSpecialAd(unittest.TestCase):

    def setUp(self) -> None:
        self.dal = TestApiSpecialad()
        self.log = MyLog.get_log()

    # 第一个用例
    def test_api_inlay_ad(self,):
        '''
        正向用例
        :return:
        '''
        # given
        url, method, data  = TestApiSpecialad.urls[0], TestApiSpecialad.methods[0], TestApiSpecialad.datas[0]

        # when
        res = ConfigHttp(method=method, url=url, params=data).request().json()
        self.log.debug("test_api_inlay_ad 响应结果=={}".format(res))
        # then
        self.assertEqual("success",res['status'], "内置广告调用标记失败")

    def tearDown(self) -> None:
        pass