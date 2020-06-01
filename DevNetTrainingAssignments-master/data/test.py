import data_parse_script
import unittest
#from xmlunittest import XmlTestCase
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
         

         

        