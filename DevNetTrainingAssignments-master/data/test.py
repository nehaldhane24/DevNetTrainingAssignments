import data_parse_script
import unittest
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

        copy_json = json.dump(copy_json, ensure_ascii=False)
        self.assertEqual(parse_json_file(), copy_json) #check if the loaded file and hardcoded files match

        def test_read_file_data_yml(self):
            copy_yml =  { 
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
                        }  #hardcoded json file

            self.assertEqual(parse_yml_file(), copy_yml) #check if the loaded file and hardcoded files match
         

        def test_read_file_data_xml(self):
            copy_xml =  '''<?xml version="1.0" encoding="UTF-8" ?>
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
                            </root>
                        '''
            #hardcoded json file
            myroot = ET.fromstring(copy_xml)
            self.assertEqual(parse_xml_file(), myroot) #check if the loaded file and hardcoded files match

         

        
