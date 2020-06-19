import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
# def get_resource(id=None):
#     data={}
#     if id is not None:
#         data={
#             'id':id
#         }
#     resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# #id=input('Enter Emplyee ID:')
# get_resource(3)

# def get_resource_all():
#     resp=requests.get(BASE_URL+ENDPOINT)
#     print(resp.status_code)
#     print(resp.json())
# def create_resource():
#     new_emp={
#         'eno':106,
#         'ename':'Tulika',
#         'esal':100000,
#         'eaddr':'Bangalore',
#     }
#     resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# create_resource()
def update_resource(id):
    update_emp={
        'id':id,
        'esal':10000,
        'eaddr':'Hinjili',
    }
    resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(update_emp))
    print(resp.status_code)
    print(resp.json())
update_resource(8)

# def delete_resource(id):
#     resp=requests.delete(BASE_URL+ENDPOINT+str(id)+'/')
#     print(resp.status_code)
#     print(resp.json())
# delete_resource(7)