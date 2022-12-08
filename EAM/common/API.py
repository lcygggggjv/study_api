import requests

from EAM.config.config import config
import openpyxl
from openpyxl.worksheet.worksheet import Worksheet

class API:

    def tc_login(self):

        res=requests.request('post',
                             url=config.tc_sit_host,
                             json={
                              "operationName": "login",
                              "variables": {
                                "input": {
                                  "account": config.sit_account,
                                  "password": config.sit_password,
                                  "tenantCode": config.sit_tentcode
                                }
                              },
                              "query": "mutation login($input: LoginInput!) {\n  login(input: $input) {\n    token\n    userId\n    __typename\n  }\n}"
                            })


        result=res.json()

        token=result['data']['login']['token']
        return token


    def read_excel(self,filename,sheetname):

        workbook=openpyxl.load_workbook(filename)   #取文件的名称
        sheet:Worksheet =workbook[sheetname]        #取sheet页

        data=list(sheet.values)         #取sheet内容，转成列表

        title=data[0]   #标题只取第0个
        rows=data[1:]  #取内容从第一个开始


        data=[dict(zip(title,row))  for row  in rows]       #先for循环，取列表内容，获取每一行内容，zip函数，依次拼接表头，转成字典格式，列表嵌套

        return data

if __name__ == '__main__':
    ad=API()
    token=ad.tc_login()
    exs=ad.read_excel(config.login_file,'login')
    print(exs)