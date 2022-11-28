

import requests


def tc_login():


    res=requests.request('post',
                         url='https://test2.teletraan.io/graphql/?login',
                         headers={"content-type":"application/json"},
                         json={
                          "operationName": "login",
                          "variables": {
                            "input": {
                              "account": "eam115",
                              "password": "teletraan",
                              "tenantCode": "110"
                            }
                          },
                          "query": "mutation login($input: LoginInput!) {\n  login(input: $input) {\n    token\n    userId\n    __typename\n  }\n}"
                        })


    try:
        ss=res.json()

    except:
        raise  ValueError("响应结果不是json",res.text)

    return ss['data']['login']['token']  #token字符串



if __name__ == '__main__':

    ad=tc_login()
    print(ad)