"""
TOPIC:: Authorization OAuth2 Bearer Token - Postman Requests

Q. Why we need authorization?
    To restrict the users to do the CRUD operations on an account except the owner

    So there are some authorization techniques, one of them is BEARER Token.

Q. Bearer Token:
    Its One kind of a string as a keyword, we need to use whenever we calling any apis.

Interview Q:: What kind of authorization techniques you are using in a project?
    So, we are using "Auth Token 2"
=============================================================================================
Codes:
    Status code 200: Success working fine ---> will get for GET mostly.
    Status code 201: When something created in database ---> will get for POST.
    Status code 400: When No Access.
    Status code 404: When Authorization is not successful.
    Status code 500: When Server Issue.
=========================================================================================================
Manually in POSTMAN::

    Source: gorest.co.in
    Get Access Token:: 7bfb932f81154d98a05a718f3c12e1cee677b62c39a3fccff425771979ea92be

    Go to the source generated the access token for authorization.

Now
In postman:: created a POST call using the below resource:
Step1::

     URL: https://gorest.co.in/public/v2/users
     Headers:
        Content-Type : application/json
        Authorization : Bearer 7bfb932f81154d98a05a718f3c12e1cee677b62c39a3fccff425771979ea92be     ---> This is the new header 'Authorization' we should pass as Bearer + AccessToken
    Body > Raw :
        {
      "id": 8259973, ---> Since we are posting we dont need to keep id
      "name": "Varun",
      "email": "chidaakaash_mr_arora@stokes.test",
      "gender": "female",
      "status": "active"
    }

Step2::
    Now clicking send button, POST will send response as follows.
        Status code:  '422 '
        Status message: 'Unprocessable Entity'
        Body Response:
         [
         {"field":"email",
        "message": "has already been taken"}
        ]


    Issue --> Email is already taken


Step3:
    Now update the payload to rectify the issue occured in step2 and click send button.
    Used the below payload to send:

    {
      "name": "Varun",
      "email": "Varuntest1234@gmail.com",   ---> updated the mail
      "gender": "female",
      "status": "active"
    }

    Statu: 201
    Status Message: Created
    Body Response:

            {
        "id": 8275999, ---> unique id will be generated
        "name": "Varun",
        "email": "Varuntest1234@gmail.com",
        "gender": "female",
        "status": "active"
    }

Step4:
    Now I will fetch (GET) that newly created details using the "id" without the 'Authorization'

    URL: https://gorest.co.in/public/v2/users/8275999
     Headers:
        Content-Type : application/json

    Click send

    Response:
        status: 404
        message: Not Found
        Body:
            {
                "message": "Resource not found"
            }

    Issue Reason---> since there is no authorization it won't fetch the data.

Step5:
    Now GET the data with Authorization token

    URL: https://gorest.co.in/public/v2/users/8275999
     Headers:
        Content-Type : application/json
        Authorization : Bearer 7bfb932f81154d98a05a718f3c12e1cee677b62c39a3fccff425771979ea92be

    Click send

    Response:

        Status: 200
        Message: OK
        Body:
        {
        "id": 8275999, ---> unique id will be generated
        "name": "Varun",
        "email": "Varuntest1234@gmail.com",
        "gender": "female",
        "status": "active"
    }

SO, This is how basically we do it manually, now we will do it in Automation.
"""
