import json

import pytest
import requests

from EAM.common.API import API
from EAM.read_excel.test_read_excel import read_excel

from EAM.config.config import config

cases=read_excel(config.file_dir,'area')

@pytest.mark.usefixtures('TC_login')  #夹具，传入conftest的登录前置
class Test_area(API):


    @pytest.mark.parametrize('item',cases[:3])  #使用pytest的parametize方法，传入列表，以字符串形式，
    def test_create(self,item,TC_login):

        data1=json.loads(item['data'])  #转成字典

        res=requests.request('post',
                             url=item['url'],
                             headers={"Authorization":f"bearer {TC_login}"},
                             json={
                                  "operationName": "createThingArea",
                                  "variables": {
                                    "input": {
                                      "code": data1['code'],
                                      "name": data1['name'],
                                      "parentId": data1['parentId']
                                    }
                                  },
                                  "query": "mutation createThingArea($input: CreateThingAreaInput!) {\n  createThingArea(input: $input)\n}"
                                })


        actual=res.json()

        if actual['data']:
            actual=actual['data'].keys()

        elif actual['errors']:
            actual=actual['errors'][0]['message']
        else:
            actual=actual['error']['errors'][0]['message']


        expected=item['expected']

        assert expected in actual


    @pytest.mark.parametrize('item',cases[3:5])
    def test_update(self,item,TC_login):

        data2=json.loads(item['data'])

        rea=requests.request('post',
                             url=item['url'],
                             headers={"Authorization":f"bearer {TC_login}"},
                             json={
                                  "operationName": "updateThingArea",
                                  "variables": {
                                    "input": {
                                      "code": data2['code'],
                                      "id": data2['id'],
                                      "name": data2['name']
                                    }
                                  },
                                  "query": "mutation updateThingArea($input: UpdateThingAreaInput!) {\n  updateThingArea(input: $input)\n}"
                                })

        actual=rea.json()

        if actual['data']:
            actual=actual['data'].keys()

        elif actual['errors']:
            actual=actual['errors'][0]['message']

        else:
            actual=actual['error']['errors'][0]['message']

        expected=item['expected']

        assert  expected in  actual












# class Test_area(API):
#
#     def  setup_method(self):
#
#         self.token=self.tc_login()
#
#     @pytest.mark.parametrize('item',cases[:3])
#     def test_create(self,item):
#
#         data1=json.loads(item['data'])
#
#         res=requests.request('post',
#                              url=item['url'],
#                              headers={"Authorization":f"bearer {self.token}"},
#                              json={
#                                   "operationName": "createThingArea",
#                                   "variables": {
#                                     "input": {
#                                       "code": data1['code'],
#                                       "name": data1['name'],
#                                       "parentId": data1['parentId']
#                                     }
#                                   },
#                                   "query": "mutation createThingArea($input: CreateThingAreaInput!) {\n  createThingArea(input: $input)\n}"
#                                 })
#
#
#         actual=res.json()
#
#         if actual['data']:
#             actual=actual['data'].keys()
#
#         elif actual['errors']:
#             actual=actual['errors'][0]['message']
#         else:
#             actual=actual['error']['errors'][0]['message']
#
#
#         expected=item['expected']
#
#         assert expected in actual
#
#
#     @pytest.mark.parametrize('item',cases[3:5])
#     def test_update(self,item):
#
#         data2=json.loads(item['data'])
#
#         rea=requests.request('post',
#                              url=item['url'],
#                              headers={"Authorization":f"bearer {self.token}"},
#                              json={
#                                   "operationName": "updateThingArea",
#                                   "variables": {
#                                     "input": {
#                                       "code": data2['code'],
#                                       "id": data2['id'],
#                                       "name": data2['name']
#                                     }
#                                   },
#                                   "query": "mutation updateThingArea($input: UpdateThingAreaInput!) {\n  updateThingArea(input: $input)\n}"
#                                 })
#
#         actual=rea.json()
#
#         if actual['data']:
#             actual=actual['data'].keys()
#
#         elif actual['errors']:
#             actual=actual['errors'][0]['message']
#
#         else:
#             actual=actual['error']['errors'][0]['message']
#
#         expected=item['expected']
#
#         assert  expected in  actual