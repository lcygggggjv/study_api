import json
import unittest

import requests

from EAM.common.API import API
from EAM.read_excel.test_read_excel import read_excel
from EAM.config.config import config
from unittestreport import list_data,ddt


cases=read_excel(config.file_dir,'area')


@ddt
class Test_area(unittest.TestCase,API):


    def setUp(self) -> None:

        self.token=self.tc_login()

    @list_data(cases[:3])
    def test_area_01(self,item):


        data2=json.loads(item['data'])


        res=requests.request('post',
                             url=item['url'],
                             headers={"Authorization":f"bearer {self.token}"},
                             json={
                                  "operationName": "createThingArea",
                                  "variables": {
                                    "input": {
                                      "code": data2['code'],
                                      "name": data2['name'],
                                      "parentId": data2['parentId']
                                    }
                                  },
                                  "query": "mutation createThingArea($input: CreateThingAreaInput!) {\n  createThingArea(input: $input)\n}"
                                })

        actual=res.json()
        print(actual)
        if actual['data']:
            print('pass')
            actual=actual['data'].keys()

        elif actual['errors']:
            actual=actual['errors'][0]['message']

        else:
            actual=actual['error']['errors'][0]['message']

        print(actual)
        expected=item['expected']
        print(expected)
        self.assertEqual(expected in  actual,True)


    @list_data(cases[3:5])
    def  test_02_update(self,item):

        data1=json.loads(item['data'])

        rea=requests.request('post',
                             url=item['url'],
                             headers={"Authorization":f"bearer {self.token}"},
                             json={
                                  "operationName": "updateThingArea",
                                  "variables": {
                                    "input": {
                                      "code": data1['code'],
                                      "id": data1['id'],
                                      "name": data1['name']
                                    }
                                  },
                                  "query": "mutation updateThingArea($input: UpdateThingAreaInput!) {\n  updateThingArea(input: $input)\n}"
                                })

        actual=rea.json()
        print(actual)
        if actual['data']:
            actual=actual['data'].keys()

        elif actual['errors']:
            actual=actual['errors'][0]['message']

        else:
            actual=actual['erroor']['errors'][0]['message']
        print(actual)
        expected=item['expected']
        print(expected)
        self.assertIn(expected , actual)