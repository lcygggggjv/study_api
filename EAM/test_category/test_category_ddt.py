import json
import unittest

import requests

from EAM.common.API import API
from unittestreport import list_data,ddt

from EAM.config.config import config
from EAM.read_excel.test_read_excel import read_excel

cases=read_excel(config.login_file,'category')

print(cases)
@ddt
class test_category(unittest.TestCase,API):


    def setUp(self) -> None:  #函数前置

        self.token=self.tc_login()   #继承api类，实例函数,实例token，下面用到

    @list_data(cases)
    def test_01(self,item):


        # data=item["data"]
        data1=json.loads(item["data"])

        res=requests.request('post',
                             url=config.tc_sit_host,
                             headers={"Authorization":f"bearer {self.token}"}, #请求头获取上面实例的token
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


        # try:
        actual=res.json()

        # except Exception as e:
        #     actual=res.text

        if actual["data"]:
            actual=actual["data"]

        elif actual["errors"][0]["message"]:
            actual=actual["errors"][0]["message"]

        else:
            actual=actual["error"]["errors"][0]["message"]

        print(actual)
        expected=item["expected"]
        print(expected)
        self.assertEqual(expected in actual,True)



