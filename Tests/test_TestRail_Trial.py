from Libs.CoreLibs.testrail import *
import pprint

client = APIClient('https://vadimbotestrailtraining.testrail.io')
client.user = 'rsmrostov@front.ru'
client.password = 'WYayHVIgoQBn.FLSl5xU'

# case = client.send_get('get_case/2')
# print(case)

cases =client.send_get('get_cases/1')# print all the test cases in test plan 1
id_list = []
for c in cases:
    test_id = (c['id'])
    id_list.append(test_id)
print(id_list)