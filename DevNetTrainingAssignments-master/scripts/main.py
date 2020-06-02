import getData
if __name__ == '__main__':
    token = getData.generate_token('https://sandboxdnac2.cisco.com/api/system/v1/auth/token').text
    response = getData.getData('https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device',token)
    print("Data retreived from get request is : ")
    data = response.json()
    print(data)
    print("Status code = ", response.status_code)
    getData.printData(data)
    
    
 

