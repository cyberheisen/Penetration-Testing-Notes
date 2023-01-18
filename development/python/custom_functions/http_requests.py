import requests
from requests.exceptions import Timeout

proxies = {'http':'http://127.0.0.1:8080','https':'https://127.0.0.1:8080'}
timeout = 5 # This value can be modified for time based blind SQLi
headers = {'Content-Type':'application/x-www-form-urlencoded'}

def http_request(url,method='get',data=None,headers=None,proxies=None,timeout=None):
     
    try:
        # POST Method        
        if method.lower() == 'post':
            res = requests.post(url,data,headers=headers,proxies=proxies,timeout=timeout)
        
        # Default GET Method
        else:
            res = requests.get(url,headers=headers,proxies=proxies,timeout=timeout)
        return res
        
    except Exception as error:
        return error
      
      
# sample use
url = 'http://www.google.com'
response = http_request(url)
print(response.text)
