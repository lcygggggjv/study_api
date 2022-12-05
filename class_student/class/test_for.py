

#
# a={"kk":"good","yy":"99","lcy":"777"}


error={'errors': [{'message': '企业标识符错误，请重新填写', 'extensions': {'code': 'DOWNSTREAM_SERVICE_ERROR', 'serviceName': 'iam-be'}}]}
success={'data': {'login': {'__typename': 'AuthInfo','token': '2ZjxLHcKCLOp6xZCnzmNHyP8YtSvgCRd', 'userId': '09ad4dcd-b1e1-4da5-ac42-c41f9f8c7b14'}}}

print(type(error['errors'][0]['message']))
print(type(success['data']['login']['__typename']))

# for k,v  in  a.items():
#     print(k,v)

c=(1,2,'kk')  #索引·

print(c[0])