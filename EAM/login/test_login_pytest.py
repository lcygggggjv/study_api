import json

import pytest
import requests

from EAM.read_excel.test_read_excel import read_rxcel
from EAM.config.config import config


cases=read_rxcel(config.login_file,'login')



class Test_login():

    @pytest.mark.parametrize('item',cases)   #获取cases字典值，以字符串传 pytest驱动
    def test_login_1(self,item):

        data2=item['data']   #从上面item获取到 data内容，

        data1=json.loads(data2)  #转换成字典
        print(data1['account'])
        url=item['url']
        mathod=item['method']
        res=requests.request(method=mathod,
                             url=url,
                             json={
                              "operationName": "login",
                              "variables": {
                                "input": {
                                  "account": data1['account'],
                                  "password": data1['password'],
                                  "tenantCode": data1['tenantCode']
                                }
                              },
                              "query": "mutation login($input: LoginInput!) {\n  login(input: $input) {\n    token\n    userId\n    __typename\n  }\n}"
                            })

        try:
            actual=res.json()

        except  Exception as e:
            actual=res.text
        print(actual)
        expected=item['expected']   #用例是关键字，data，error
        print(expected)


        assert  expected in actual    #判断实际结果包含预期结果


