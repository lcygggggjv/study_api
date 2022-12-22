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



    def canborrow_thing(self,token):

        url="https://teamsit.teletraan.io/graphql/?thingList"
        res=requests.request('post',
                             url=url,
                             headers={"Authorization":f"bearer {token}"},
                             json={
                                  "operationName": "thingList",
                                  "variables": {
                                    "filter": {
                                      "canBorrowed": True,
                                      "dataRangeLimit": False
                                    },
                                    "limit": 50,
                                    "offset": 0
                                  },
                                  "query": "query thingList($filter: ThingFilterInput, $limit: Int, $offset: Int, $orderBy: [String!]) {\n  thingList(filter: $filter, limit: $limit, offset: $offset, orderBy: $orderBy) {\n    data {\n      ...thing\n      __typename\n    }\n    totalCount\n    __typename\n  }\n}\n\nfragment thing on Thing {\n  storageAddr\n  canOperateBorrowed\n  codePrefix\n  name\n  code\n  id\n  currentThingBorrow {\n    expected\n    borrower {\n      id\n      name\n      jobNumber\n      organizations {\n        id\n        name\n        __typename\n      }\n      __typename\n    }\n    departmentOfApplicant {\n      id\n      name\n      __typename\n    }\n    __typename\n  }\n  attachment {\n    name\n    id\n    __typename\n  }\n  department {\n    id\n    name\n    code\n    parentID\n    pathName\n    __typename\n  }\n  administrator {\n    id\n    name\n    __typename\n  }\n  manager {\n    id\n    name\n    jobNumber\n    organizations {\n      id\n      name\n      departmentId\n      __typename\n    }\n    __typename\n  }\n  area {\n    id\n    name\n    code\n    __typename\n  }\n  category {\n    id\n    name\n    pathInfo {\n      pathName\n      __typename\n    }\n    __typename\n  }\n  thingGroup {\n    name\n    id\n    parentId\n    __typename\n  }\n  groupFile {\n    name\n    file {\n      name\n      id\n      url\n      length\n      __typename\n    }\n    isCompleteFile\n    __typename\n  }\n  maintainer {\n    id\n    name\n    __typename\n  }\n  accountingDepartment {\n    id\n    name\n    __typename\n  }\n  image {\n    id\n    name\n    url\n    __typename\n  }\n  specification\n  modelNum\n  acceptanceAt\n  accountType\n  activatedAt\n  alertAt\n  applyForPurchaseAt\n  applyForPurchaseNum\n  arrivedAt\n  assetNormalizationAt\n  bookValue\n  brand\n  calibrateCode\n  calibrateMethod\n  calibrateResult\n  calibrateState\n  canCalibrate\n  calibrateRepeat {\n    frequency\n    period\n    __typename\n  }\n  isCalibrationExpired\n  canBorrowed\n  code\n  companyID\n  contractNum\n  depreciationOfYear\n  depreciationRate\n  depreciationRateOfMonth\n  desc\n  distributor\n  fieldData\n  finalValue\n  fuselageCode\n  id\n  installedAt\n  isCalibrationExpired\n  isCompleteFile\n  isDeleted\n  isLent\n  lastCalibrateAt\n  leaseBeginAt\n  leaseFinishAt\n  leaseNum\n  machineNumber\n  manufacturer\n  modelNum\n  name\n  nextCalibrateAt\n  onState\n  parentThingId\n  poNum\n  predictResidualRate\n  produceAt\n  purchasePrice\n  purchaseType\n  purchasedAt\n  qrCode\n  sapThingCode\n  serialNumber\n  specification\n  storageAddr\n  storageType\n  subThingId\n  thingSubjectCode\n  transferAt\n  usedYear\n  warrantyInstitutions\n  warrantyMethod\n  yearsOfUse\n  performanceStatus\n  warrantyStartAt\n  warrantyPeriod {\n    period\n    frequency\n    __typename\n  }\n  warrantyDeadlineAt\n  warrantyRemindPeriod {\n    period\n    frequency\n    __typename\n  }\n  __typename\n}"
                                })

        thinglist=res.json()

        return thinglist['data']['thingList']['data'][0]

if __name__ == '__main__':
    ad=API()
    token=ad.tc_login()

    thin=ad.canborrow_thing(token)

    print(thin)