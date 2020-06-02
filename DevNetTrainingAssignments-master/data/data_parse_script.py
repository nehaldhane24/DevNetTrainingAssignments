import json
import xml.etree.ElementTree as ET
import yaml


def parse_json_file():
    print("Printing data from json file : ")
    with open('D:/DevNetTrainingAssignments-master/data/db.json') as data : #open the json file in read mode
        data_retreived = json.load(data) #retreive the data in json object format
        #print(data_retreived) #print the retreived data 
        return data_retreived
        
def parse_xml_file():
    print("Printing data from xml file : ")
    with open('D:/DevNetTrainingAssignments-master/data/db.xml') as xmlfile : #open the xml file in read mode
       tree = ET.parse(xmlfile)
       root = tree.getroot()
       for i in root: #iterate all the roots
           print(i.tag, i.attrib)
           for j in i : #iterate all the chidren
               print(j.tag,int(j.text))
           print()
       print("-------------------------------------------------")
      
def parse_yml_file():
    print("Printing data from yml file : ")
    with open('D:/DevNetTrainingAssignments-master/data/db.yml','r') as ymlfile : #open the yml file in read mode
        data = yaml.safe_load(ymlfile) #retreive the data in yml object format
        #print(data) #print the retreived data 
        return data

print(parse_json_file())
print("-------------------------------------------------")
parse_xml_file()
print(parse_yml_file())

'''
output:

Printing data from json file :
{'ACCT100': {'paid': 60, 'due': 100}, 'ACCT200': {'paid': 70, 'due': 60}, 'ACCT300': {'paid': 0, 'due': 0}}
-------------------------------------------------
Printing data from xml file :
ACCT400 {'extra': 'fun'}
paid 600
due 10000

ACCT500 {}
paid 70
due 40

ACCT600 {}
paid 0
due 0

-------------------------------------------------
Printing data from yml file :
d:/DevNetTrainingAssignments-master/data/data_parse_script.py:27: YAMLLoadWarning: calling yaml.load() without Loader=... is deprecated, as the default Loader is unsafe. Please read https://msg.pyyaml.org/load for full details.
  data = yaml.load(ymlfile) #retreive the data in yml object format
{'ACCT700': {'paid': 60, 'due': 100}, 'ACCT800': {'paid': 70, 'due': 60}, 'ACCT900': {'paid': 0, 'due': 0}}

'''

