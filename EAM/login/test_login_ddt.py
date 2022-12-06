import json
import unittest

import requests
from EAM.common.setting import logger
from unittestreport import list_data,ddt
from EAM.read_excel.test_read_excel import read_rxcel
from EAM.config.config import config

cases=read_rxcel(config.login_file,'login')



@ddt
class Test_login(unittest.TestCase):


    @list_data(cases)
    def test_login_01(self,item):

        logger.info('运行结果')
        data=item['data']  #取用例里data数据
        data1=json.loads(data)
        url = item['url']
        method=item['method']

        res=requests.request(method=method,
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
            actual=res.json()   #进行try 是json格式跳过

        except Exception as e:
            actual=res.text   #执行text格式
            # actual={msg:actual}
        print(actual)
        if actual["data"]==None:   #if判断  取实际结果里的data，正确的不是none，
            actual=actual['errors'][0]['message']
        else:
            actual=actual
        expected=item['expected'] #取用例里的预期结果
        print(expected)
        self.assertEqual(expected in actual ,True) #，对比预期结果在实际结果里


