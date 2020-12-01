# -*- codeing = utf-8

import unittest
import re


from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import TestApiSpecialcms


class TestApiSpecialCms(unittest.TestCase):

    def setUp(self) -> None:
        # self.dal = TestApiSpecialcms()  导入后直接用类属性
        self.mylog = MyLog.get_log()

    def test_api_specialcms(self):
        '''
        测试调用内置api文章
        :return:
        '''
        ts = TestApiSpecialcms
        #when
        url,data,method, expected = ts.urls[0],ts.datas[0],ts.methods[0],ts.expected[0]

        #then
        res = ConfigHttp(url=url,params=data,method=method).request()

        self.mylog.debug("-----test_api_specialcms----响应结果为{}".format(res.text))

        # reg = re.findall(r'\"single_article_title\":\".*?(?=,)\"',date)
        # date = res["result"[2][reg]]
        # print(reg)

        pattern = re.compile(r"\"single_article_title\":\"(.+?)\"")
        #
        single_article_title_list = pattern.findall(res.text)  # 列表
        # #then
        # self.assertEqual("success",res["status"],"信息调用失败")
        self.mylog.debug("-----tsingle_article_title_list----响应结果为{}".format(single_article_title_list))
        self.assertListEqual(single_article_title_list, expected)

    def tearDown(self) -> None:

        pass

    pass




