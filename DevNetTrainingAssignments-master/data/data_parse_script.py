import json
import xml.etree.ElementTree as ET
import yaml
import unittest

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
        data = yaml.load(ymlfile) #retreive the data in yml object format
        print(data) #print the retreived data 

print(parse_json_file())
print("-------------------------------------------------")

parse_xml_file()
parse_yml_file()
