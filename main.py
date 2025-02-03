import requests
from datetime import datetime

Token="hlksjdlfkilshil34lkh"
Username="spsushant"
id="graph1"

pixela_Endpoint="https://pixe.la/v1/users"
user_params={
    "token":Token,
    "username":Username,
    "agreeTermsofService":"yes",
    "notMinor":"yes"
}
response=requests.post(url=pixela_Endpoint,json=user_params)
# print(response.text)

graph_endpoint=f"{pixela_Endpoint}/{Username}/graphs"
graph_parms={
    "id":id,
    "name":"Running Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}

headers={
    "X-USER-TOKEN":Token
}
response=requests.post(url=graph_endpoint,json=graph_parms,headers=headers)
# print(response.text)

Graph_body_endpoint=f"{pixela_Endpoint}/{Username}/graphs/{id}"
today_date=datetime.now()

body_params={
    "date":today_date.strftime("%Y%m%d"),
    "quantity":input("how many km you run:")
}

response=requests.post(url=Graph_body_endpoint,json=body_params,headers=headers)
print(response.text)

update_endpoint=f"{pixela_Endpoint}/{Username}/graphs/{id}/{today_date.strftime('%Y%m%d')}"

update_parms={
    "quantity":"3"
}
# response1=requests.put(url=update_endpoint,json=update_parms,headers=headers)
# print(response1)