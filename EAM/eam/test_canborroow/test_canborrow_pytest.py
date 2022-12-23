import pytest
import requests

from EAM.common.API import API
from EAM.config.config import config
from EAM.read_excel.test_read_excel import read_excel

cases=read_excel(config.file_dir,'canborrow')


class Test_canborrow(API):


    def setup_method(self):

        self.token=self.tc_login()

        self.times=self.time_stamp()

        self.thing_id=self.canborrow_thing(self.token)


    @pytest.mark.parametrize('item',cases)
    def test_create_brw(self,item):

        url="https://teamsit.teletraan.io/graphql/?createThingBorrow"
        res=requests.request('post',
                             url=url,
                             headers={"Authorization":f"bearer {self.token}"},
                             json={
                                  "operationName": "createThingBorrow",
                                  "variables": {
                                    "input": {
                                      "attachment": [
                                        {
                                          "id": "2378"
                                        }
                                      ],
                                      "borrower": {
                                        "id": "6ca8dd0b-24ba-4a92-9437-5b161fb4894b"
                                      },
                                      "departmentOfApplicant": {
                                        "id": "183931"
                                      },
                                      "expected": {
                                        "start": 1671638400000,
                                        "end": 1672502399999
                                      },
                                      "reason": "测试",
                                      "thing": [
                                        {
                                          "id": self.thing_id
                                        }
                                      ]
                                    }
                                  },
                                  "query": "mutation createThingBorrow($input: SetThingBorrowInput!) {\n  createThingBorrow(input: $input)\n}"
                                })




