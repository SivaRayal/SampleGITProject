# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 14:54:32 2020

@author: Siva Rayal
"""
import requests,json
#file=open("PetStore_Swagger.json")
url="https://petstore.swagger.io/v2/swagger.json"
resp = requests.get(url)

SwaggerFile=resp.json()

print("Endpoints scrapped from Petstore JSON file which is availble at - ",url)
for s in SwaggerFile['paths']:
    print(s)
