import pytest
import requests

from EAM.config.config import config


@pytest.fixture
def TC_login():

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

    yield token