import requests

from EAM.config.config import config


class API:

    def tc_login(self):

        res=requests.request('post',
                             url=config.tc_sit_host,
                             json={
                              "operationName": "login",
                              "variables": {
                                "input": {
                                  "account": 'eam111',
                                  "password": 'teletraan',
                                  "tenantCode": 'cr7'
                                }
                              },
                              "query": "mutation login($input: LoginInput!) {\n  login(input: $input) {\n    token\n    userId\n    __typename\n  }\n}"
                            })

        try:
            result=res.json()

        except Exception as e:
            result=res.text
        token=result['data']['login']['token']
        return token



if __name__ == '__main__':
    ad=API()
    token=ad.tc_login()
    print(token)