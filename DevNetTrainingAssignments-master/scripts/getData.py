import requests
from base64 import b64encode
#get the token 
def generate_token(url):
    payload_data={}
    username_password = b64encode(b"dnacdev:D3v93T@wK!").decode("ascii")#base 64 encode and and then decode it to acsii as it is stored in byte string
    headers = { 'Authorization' : 'Basic %s' %  username_password}
    response = requests.request('POST', url, headers=headers, data = payload_data)
    return response
#get data using token
def getData(url,token) : 
    payload_data = {}
    headers = {
        "x-auth-token" :" " #"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI1ZWNlNTc5ODc1MTYxMjAwY2M1NzA2M2QiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlNWE0MzI1NzUxNjEyMDBjYzRhYzk1ZSJdLCJ0ZW5hbnRJZCI6IjVlNWE0MzI1NzUxNjEyMDBjYzRhYzk1YyIsImV4cCI6MTU5MTA5NTA3NywiaWF0IjoxNTkxMDkxNDc3LCJqdGkiOiI5NWQ5NzcyYS1mZDQ5LTQ3NGUtYTRjMS1iZDRmZTg1MzEwOTgiLCJ1c2VybmFtZSI6ImRuYWNkZXYifQ.INiOMzaDcsnNjTVXCNJpns2z17tYqW8uqAjBHnbXGMxElmZVoRghqw_BG6L2I17IfAvvXDKnqxRNfZFvut4xbaZUh2i0TIxLlYo4yPx5A6XHjfeELo5StIaLzc6C-2k3tpmMvyHuZNUaDPEpH9E89fJMhnRjKpWvKGcnEcbQ-ODAVc-miWtTPdg62ltPlLL9u3Dc0l6FLD5GJeI5mzk7Wu6tZl4Vra4CEJ_zM9B1hK2ox28rQ4Wdl08qb5TUSkVsoJAkBdzj2ZMYfRW8EXQvBtAI0O-oMu_Qld2SUqbTIYn7Kyv1T6xAYyS69wIz8_CgQEijtYWvacJGekJFc0o88g"
    }
    headers['x-auth-token'] = token['Token']
    response = requests.request("GET",url, headers=headers, data = payload_data)
    return(response)

#print the extracted data
def printData(data):
    for i in data['response']:
            print("{id : ",i['id'], "type : ",i['type'],"family : ",i['family'], " softwareType : ", i['softwareType'],"}")
      

