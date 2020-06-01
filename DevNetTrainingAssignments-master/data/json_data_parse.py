import json

def parse_json_file():
    print("Printing data from json file : ")
    with open('D:/DevNetTrainingAssignments-master/data/dnac_devices.json') as data : #open the json file in read mode
        data_retreived = json.load(data) #retreive the data in json object format
        #print(data_retreived) #print the retreived data
        list1=[] 
        #print(list1)
        for i in data_retreived['response']:
            print("{id : ",i['id'], "type : ",i['type'],"family : ",i['family'], " softwareType : ", i['softwareType'],"}")

parse_json_file()
'''
output:
Printing data from json file :
{id :  1904ca0d-01be-4d13-88e5-4f4f9980b512 type :  Cisco ASR 1001-X Router family :  Routers  softwareType :  IOS-XE }
{id :  181a0fcb-e56e-4833-a92a-ec9932be427c type :  None family :  None  softwareType :  None }
{id :  3ab79a68-4a3a-4cdc-b41e-eb98dabcdb84 type :  None family :  None  softwareType :  None }
{id :  7efadae4-0023-434f-8ae6-0bbc3c51ff2c type :  None family :  None  softwareType :  None }
{id :  ea400390-f224-4587-a11e-a941c68bd141 type :  None family :  None  softwareType :  None }
'''