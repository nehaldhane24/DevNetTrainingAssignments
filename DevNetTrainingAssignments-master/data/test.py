import data_parse_script
import io
import unittest 
import json
import parser
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
output :

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
.Printing data from yml file :
.
----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK

(base) D:\DevNetTrainingAssignments-master>

'''

        
