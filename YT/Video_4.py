"""
PUT Request:
-----------

Q. What is the basic difference between the PUT and POST request in testing ?
    POST is to create new data.
    PUT is to update (90% it is update) -it is also used to create also but big companies will max use it for update.

    Execution:
    When we use POST it will create the new data with payload, chances are there it might also create duplicate data
    but when we use PUT -
    1st it will check for any data is matching with the sending payload - if exist it will update else creates new data.

    So, we can say PUT can CREATE and UPDATE


idempotent?
-----------
Meaning: if same task is happening mutiple times then it considered that as a single task.
That's why we tell PUT is a idempotent and POST is not a idempotent

    Ex: if i send POST 5 times it will create 5 rows inside a server where as PUT will check for existing record and update it.
    ( PUT: It will rewrite the same work)

"""

import requests
url = r"https://fakerestapi.azurewebsites.net/api/v1/Activities/4"
head = {
    'Accept': 'text/plain',
    'Content-Type': 'application/json'
}

# ---------------- GET --------------------------------
response = requests.get(url,headers=head)
print(response.json())


print("Before Put")
# ---------------------PUT------------------------------

putPayload = {
    "id": 40,
    "title": "Varun",
    "dueDate": "2025-12-02T02:01:55.621Z",
    "completed": True
}

responsePut = requests.put(url,headers=head,json =putPayload)

print(responsePut.json())
