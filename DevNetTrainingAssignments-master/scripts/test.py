import data_parse_script
import io
import unittest 
import json
import parser
import xmltodict
#from xmlunittest import XmlTestCase
import xml.etree.ElementTree as ET
class TestMyFunctions(unittest.TestCase):
    def test_read_file_data_json(self):
        copy_json = { 
                        "ACCT100": {
                            "paid": 60,
                            "due": 100
                        },
                        "ACCT200": {
                            "paid": 70,
                            "due": 60
                        },
                        "ACCT300": {
                            "paid": 0,
                            "due": 0
                        }
                      } #hardcoded json file

        #copy_json = json.dump(copy_json)
        self.assertEqual(data_parse_script.parse_json_file(), copy_json) #check if the loaded file and hardcoded files match
   
    def test_read_file_data_xml(self):
        copy_xml = """<?xml version="1.0" encoding="UTF-8" ?>
                        <root>
                        <ACCT400 extra="fun">
                            <paid>600</paid>
                            <due>10000</due>
                        </ACCT400>
                        <ACCT500>
                            <paid>70</paid>
                            <due>40</due>
                        </ACCT500>
                        <ACCT600>
                            <paid>0</paid>
                            <due>0</due>
                        </ACCT600>
                        </root>"""#hardcoded xml file
        
        data1 = json.dumps(data_parse_script.parse_xml_file())
        copy_xml = json.dumps(xmltodict.parse(copy_xml))#convert expected file to dictionary for comparison
        self.assertEqual(data1, copy_xml) #check if the loaded file and hardcoded files match
        
    def test_read_file_data_yml(self):
        copy_yml =  { 
                        "ACCT700": {
                            "paid": 60,
                            "due": 100
                        },
                        "ACCT800": {
                            "paid": 70,
                            "due": 60
                        },
                        "ACCT900": {
                            "paid": 0,
                            "due": 0
                        }
                    }  #hardcoded json file
        
        data1 = json.dumps(data_parse_script.parse_yml_file())
        copy_yml = json.dumps(copy_yml)
        #print((data1))
        #print((copy_yml))
        self.assertEqual(data1, copy_yml) #check if the loaded file and hardcoded files match
       
 
        
unittest.main()
'''
output
(base) D:\DevNetTrainingAssignments-master>conda activate base

(base) D:\DevNetTrainingAssignments-master>C:/Users/Home/Miniconda3/python.exe d:/DevNetTrainingAssignments-master/data/test.py
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
{'ACCT700': {'paid': 60, 'due': 100}, 'ACCT800': {'paid': 70, 'due': 60}, 'ACCT900': {'paid': 0, 'due': 0}}
Printing data from json file :
.Printing data from xml file :
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
.Printing data from yml file :
.
----------------------------------------------------------------------
Ran 3 tests in 0.009s

OK

(base) D:\DevNetTrainingAssignments-master>

'''
         

        
