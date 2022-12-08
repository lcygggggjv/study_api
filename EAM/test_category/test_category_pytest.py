import json

import pytest
import requests

from EAM.common.API import API
from EAM.read_excel.test_read_excel import read_excel
from EAM.config.config import config

cases=read_excel(config.login_file,'category')


@pytest.mark.usefixtures('tc_login2')   #把对应的前置放在里面，获取的token
class Test_category(API):


    @pytest.mark.parametrize('data',cases)  #pytest的方法，传进字典，以字符串
    def test_01_category(self,data,tc_login2):  #传入参数化的data，  和token


        data1=json.loads(data['data'])  #取没个用例里的data

        # data2=json.loads(data1)  #转成字典

        res=requests.request('post',
                             url=config.tc_sit_host,
                             headers={"Authorization":f"bearer {tc_login2}"},  #格式化传入token
                             json={
                              "operationName": "createThingCategory",
                              "variables": {
                                "input": {
                                  "code": data1["code"],
                                  "name": data1["name"],
                                  "parentId": data1["parentId"]
                                }
                              },
                              "query": "mutation createThingCategory($input: CreateThingCategoryInput!) {\n  createThingCategory(input: $input)\n}"
                            })

        actual=res.json()
        print(actual)
        if actual['data']:
            actual=actual['data']

        elif actual['errors'][0]['message']:
            actual=actual['errors'][0]['message']
        else:
            actual=actual['error']['errors'][0]['message']

        expected=data['expected']  #data里的
        print(expected)
        assert  expected == actual




# class Test_category(API):
#
#
#     def setup(self):
#
#         self.token=self.tc_login()
#
#     @pytest.mark.parametrize('data',cases)  #pytest的方法，传进字典，以字符串
#     def test_01_category(self,data):
#
#
#         data1=json.loads(data['data'])  #取没个用例里的data
#
#         # data2=json.loads(data1)  #转成字典
#
#         res=requests.request('post',
#                              url=config.tc_sit_host,
#                              headers={"Authorization":f"bearer {self.token}"},
#                              json={
#                               "operationName": "createThingCategory",
#                               "variables": {
#                                 "input": {
#                                   "code": data1["code"],
#                                   "name": data1["name"],
#                                   "parentId": data1["parentId"]
#                                 }
#                               },
#                               "query": "mutation createThingCategory($input: CreateThingCategoryInput!) {\n  createThingCategory(input: $input)\n}"
#                             })
#
#         actual=res.json()
#
#         if actual['data']:
#             actual=actual['data']
#
#         elif actual['errors'][0]['message']:
#             actual=actual['errors'][0]['message']
#         else:
#             actual=actual['error']['errors'][0]['message']
#
#         expected=data['expected']
#
#         assert  expected == actual





