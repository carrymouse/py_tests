# -*- codeing = utf-8


import unittest

from ddt import ddt, file_data

from apitest.api.debugtalk import dbshop_login
from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import TestApijobAddgoodsask


@ddt
class TestDbApijobAddgoodsask(unittest.TestCase):

    def setUp(self) -> None:
        self.mylog = MyLog.get_log()

    @file_data(r"D:\cs_apitest\cs_apitest\apitest\data\test_apijob_user.json")
    def test_apijob_addgoodsask(self, user_name, user_password, user_unionid, goods_ask_content, goods_id):

        login_res = dbshop_login(user_name, user_password, user_unionid)

        token = login_res["result"]["user_token"]

        url, data, method, expected = TestApijobAddgoodsask.urls[0], TestApijobAddgoodsask.datas[0], \
                                      TestApijobAddgoodsask.methods[0], TestApijobAddgoodsask.expecteds[0]

        data.update({
            "user_token": token,
            "goods_id": goods_id,
            "goods_ask_content": goods_ask_content
        })

        res = ConfigHttp(url=url, data=data, method=method).request()

        self.mylog.debug("----test_apijob_addgoodsask----,相应结果为{}".format(res))

        self.assertEqual(["添加商品咨询成功!"], expected)


