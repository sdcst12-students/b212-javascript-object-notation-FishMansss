#!python3
import requests
import json

# we can use requests to retrieve json encoded data from the internet
# there are different methods that we can retrieve the data with: POST and GET
# You can google the difference between POST and GET requests

req = requests.get('http://sdcaf.hungrybeagle.com/menu.php')
data = req.text
decoded = json.loads(data)

print(decoded['menu'][0])
for i in range(len(decoded['menu'])):
        for key, value in decoded['menu'][i].items():
                print(f'{key}\t{value}')
      
# Use the json encoded data that is retrieved from this website and print out the weekly menu
# You will need to decipher the json decoded data to determine what information the 
# dictionary object contains

