"""
This is regarding POST request

Steps:
1. 1st we need to give the path ---> URL
2. We need to have the payload - we called it as get payload  or Request Payload

Responses we get:
1. Curl body
2. Request URL
3. Server Response code
4. Server Response Details (Response Body & Response Headers)


IN Postman:
1. Change the status
2. Provide the url
3. Provide the body in raw in jason format
4. Provide the headers (Accept & Content-type)
"""

import requests
url = r"https://fakerestapi.azurewebsites.net/api/v1/Activities/"
head = {
    'Accept': 'text/plain',
    'Content-Type': 'application/json'
}

request_payload = {
    "id": 31,
    "title": "Testing the id 31",
    "dueDate": "2025-12-02T02:01:55.621Z",
    "completed": True
}

response = requests.post(url,headers=head,json = request_payload)
print(response.status_code)
print(response.json())
responseData = response.json()

assert response.status_code == 200, f"status code isn't matching 200"
assert responseData['id'] == 31, "id is not matching"