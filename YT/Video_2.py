import json
import requests


"""
This is regarding GET request

Source1: https://fakerestapi.azurewebsites.net/index.html
Source2: https://www.youtube.com/watch?v=GJGUQ5IP6JI&list=PLHT5rv7PEE4N3ol8lBoxHBmzWvVW2UwmC&index=3
"""

url = r"https://fakerestapi.azurewebsites.net/api/v1/Activities/4"
head = {
    'Accept':'text/plain'
}
response = requests.get(url,headers=head)

print(response.status_code)
data = response.json()
print(data)
print(json.dumps(data,indent = 4))


assert response.status_code == 200