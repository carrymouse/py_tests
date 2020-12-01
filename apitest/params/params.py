# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang

"""
定义所有测试数据
"""
import os

from apitest.params import tools

path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def _getParameter(name):
    data = tools.GetPages().get_page_list()
    # pprint(data)
    param = data[name]
    return param

# class TestConn:
#
#     params = _getParameter('test_conn1')
#     urls = []
#     datas = []
#     headers = []
#     names= []
#     methods= []
#     expecteds = []
#     for i in range(0, len(params)):
#         urls.append(params[i]["test"]["request"].get("url"))
#         datas.append(params[i]["test"]["request"].get("data"))
#         headers.append(params[i]["test"]["request"].get("headers"))
#         methods.append(params[i]["test"]["request"].get("method"))
#         expecteds.append(params[i]["test"]["request"].get("expected"))
#         names.append(params[i]["test"].get("name"))
#
# class TestConnCase:
#     params = _getParameter('test_conn1')
#     methods = []
#     for i in range(0, len(params)):
#         methods.append(params[i]["test"]["request"].get("method"))

# class TestApiStatistics:
#     params = _getParameter('test_api_statistics')
#     urls = []
#     datas = []
#     methods= []
#     for i in range(0, len(params)):
#         urls.append(params[i]["test"]["request"].get("url"))
#         datas.append(params[i]["test"]["request"].get("data"))
#         methods.append(params[i]["test"]["request"].get("method"))

# class TestApiSpecialad:
#     params = _getParameter('test_api_specialad')
#     urls = []
#     datas = []
#     methods= []
#     for i in range(0, len(params)):
#         urls.append(params[i]["test"]["request"].get("url"))
#         datas.append(params[i]["test"]["request"].get("data"))
#         methods.append(params[i]["test"]["request"].get("method"))

# class TestApiSpecialcms:
#     params = _getParameter('test_api_specialcms')
#     urls = []
#     datas = []
#     methods = []
#     expected =[]
#     for i in range(0, len(params)):
#         urls.append(params[i]["test"]["request"].get("url"))
#         datas.append(params[i]["test"]["request"].get("data"))
#         methods.append(params[i]["test"]["request"].get("method"))
#         expected.append(params[i]["test"]["request"].get("expected"))
#
# class TestApigoodsClass:
#
#     params = _getParameter('test_api_goodsclass')
#     urls = []
#     datas = []
#     methods= []
#     #expecteds = []
#     for i in range(0, len(params)):
#         urls.append(params[i]["test"]["request"].get("url"))
#         datas.append(params[i]["test"]["request"].get("data"))
#         methods.append(params[i]["test"]["request"].get("method"))
#         #expecteds.append(params[i]["test"]["request"].get("expected"))

# class TestApispecialGoods:
#
#     params = _getParameter('test_api_specialgoods')
#     urls = []
#     datas = []
#     methods= []
#     #expecteds = []
#     for i in range(0, len(params)):
#         urls.append(params[i]["test"]["request"].get("url"))
#         datas.append(params[i]["test"]["request"].get("data"))
#         methods.append(params[i]["test"]["request"].get("method"))
#         #expecteds.append(params[i]["test"]["request"].get("expected"))

class TestApiLogin:

    params = _getParameter('test_api_login')
    urls = []
    datas = []
    methods= []
    #expecteds = []
    for i in range(0, len(params)):
        urls.append(params[i]["test"]["request"].get("url"))
        datas.append(params[i]["test"]["request"].get("data"))
        methods.append(params[i]["test"]["request"].get("method"))
        #expecteds.append(params[i]["test"]["request"].get("expected"))

class TestApiLogout:

    params = _getParameter('test_api_logout')
    urls = []
    datas = []
    methods= []
    #expecteds = []
    for i in range(0, len(params)):
        urls.append(params[i]["test"]["request"].get("url"))
        datas.append(params[i]["test"]["request"].get("data"))
        methods.append(params[i]["test"]["request"].get("method"))
        #expecteds.append(params[i]["test"]["request"].get("expected"))

class TestApigoodsInfo:

    params = _getParameter('test_api_goodsinfo')
    urls = []
    datas = []
    methods= []
    #expecteds = []
    for i in range(0, len(params)):
        urls.append(params[i]["test"]["request"].get("url"))
        datas.append(params[i]["test"]["request"].get("data"))
        methods.append(params[i]["test"]["request"].get("method"))
        #expecteds.append(params[i]["test"]["request"].get("expected"))

class TestAddgoodsask:

    params = _getParameter('test_api_addgoodsask')
    urls = []
    datas = []
    methods= []
    expecteds = []
    for i in range(0, len(params)):
        urls.append(params[i]["test"]["request"].get("url"))
        datas.append(params[i]["test"]["request"].get("data"))
        methods.append(params[i]["test"]["request"].get("method"))
        expecteds.append(params[i]["test"]["request"].get("expected"))


class TestApiSubmitOrdergoodsComment:

    params = _getParameter('test_api_submitordergoodscomment')
    urls = []
    datas = []
    methods= []
    expecteds = []
    for i in range(0, len(params)):
        urls.append(params[i]["test"]["request"].get("url"))
        datas.append(params[i]["test"]["request"].get("data"))
        methods.append(params[i]["test"]["request"].get("method"))
        expecteds.append(params[i]["test"]["request"].get("expected"))

class TestApiOrderlist:

    params = _getParameter('test_api_orderlist')
    urls = []
    datas = []
    methods= []
    expecteds = []
    for i in range(0, len(params)):
        urls.append(params[i]["test"]["request"].get("url"))
        datas.append(params[i]["test"]["request"].get("data"))
        methods.append(params[i]["test"]["request"].get("method"))
        expecteds.append(params[i]["test"]["request"].get("expected"))

class TestApihomeGoodsAskDel:

    params = _getParameter('test_api_homegoodsaskdel')
    urls = []
    datas = []
    methods= []
    expecteds = []
    for i in range(0, len(params)):
        urls.append(params[i]["test"]["request"].get("url"))
        datas.append(params[i]["test"]["request"].get("data"))
        methods.append(params[i]["test"]["request"].get("method"))
        expecteds.append(params[i]["test"]["request"].get("expected"))


class TestApijobLogout:

    params = _getParameter('test_apijob_logout')
    urls = []
    datas = []
    methods= []
    expecteds = []
    for i in range(0, len(params)):
        urls.append(params[i]["test"]["request"].get("url"))
        datas.append(params[i]["test"]["request"].get("data"))
        methods.append(params[i]["test"]["request"].get("method"))
        expecteds.append(params[i]["test"]["request"].get("expected"))

class TestApijobLogin:

    params = _getParameter('test_apijob_login')
    urls = []
    datas = []
    methods= []
    expecteds = []
    for i in range(0, len(params)):
        urls.append(params[i]["test"]["request"].get("url"))
        datas.append(params[i]["test"]["request"].get("data"))
        methods.append(params[i]["test"]["request"].get("method"))
        expecteds.append(params[i]["test"]["request"].get("expected"))

class TestApijobAddgoodsask:

    params = _getParameter('test_apijob_addgoodsask')
    urls = []
    datas = []
    methods= []
    expecteds = []
    for i in range(0, len(params)):
        urls.append(params[i]["test"]["request"].get("url"))
        datas.append(params[i]["test"]["request"].get("data"))
        methods.append(params[i]["test"]["request"].get("method"))
        expecteds.append(params[i]["test"]["request"].get("expected"))

class TestApiaddressList:

    params = _getParameter('test_api_addresslist')
    urls = []
    datas = []
    methods= []
    expecteds = []
    for i in range(0, len(params)):
        urls.append(params[i]["test"]["request"].get("url"))
        datas.append(params[i]["test"]["request"].get("data"))
        methods.append(params[i]["test"]["request"].get("method"))
        expecteds.append(params[i]["test"]["request"].get("expected"))

if __name__ == '__main__':
    icm = TestApiaddressList()
    print(icm.datas[0])
    print(icm.urls[0])
    print(icm.methods[0])
    print(icm.expecteds[0])

    pass
