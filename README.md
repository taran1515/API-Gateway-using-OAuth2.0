
API-Gateway-using-OAuth2.0 
====================


***If you are facing one or more of the following***:
* Your Django app exposes a web API you want to protect with OAuth2 authentication,
* You need to implement an OAuth2 authorization server to provide tokens management for your infrastructure,

Django OAuth Toolkit provides out of the box all the endpoints, data and logic needed to add OAuth2 capabilities to your Django projects. Django OAuth Toolkit makes extensive use of the excellent [OAuthLib](https://github.com/oauthlib/oauthlib), so that everything is [rfc-compliant](https://tools.ietf.org/html/rfc6749).

### OAuth defines four roles: ###

* ***Resource Owner***
      An entity capable of granting access to a protected resource.
      When the resource owner is a person, it is referred to as an
      end-user.

* ***Resource server***
      The server hosting the protected resources, capable of accepting
      and responding to protected resource requests using access tokens.

* ***Client***
      An application making protected resource requests on behalf of the
      resource owner and with its authorization.  The term "client" does
      not imply any particular implementation characteristics (e.g.,
      whether the application executes on a server, a desktop, or other
      devices).

* ***Authorization Server***
      The server issuing access tokens to the client after successfully
      authenticating the resource owner and obtaining authorization.
      
The Authorization Flow lloks like : [this](https://tools.ietf.org/html/rfc6749#section-1.2)

### Grant Types ###
  * ***Authorization Code***
  * ***Implicit***
  * ***Resource Owner Password Credentials***
  * ***Client Credentials***
  
  The project uses Resource Owner Password Credentials as grant types. The protocol flow looks somewhat [like](https://drive.google.com/open?id=1gYDAA0WaOktyR2MTMUhNuxvcffnpuw1u): 

## Usage ##

### Installations ###

Clone the repository:

```
$ git clone https://github.com/taran1515/API-Gateway-using-OAuth2.0.git
```

Create a virtual environment and install requirements:

```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
Navigate to manage.py directory.
Migrate the database and createsuperuser:

```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
```

Now run the server and login to the admin page and go to authorization server
```
$ python manage.py runserver
http://localhost:8000/admin/
http://localhost:8000/o/applications/
```
Now create new application with following configuration and make not of Client ID and Client Secret
```
{
    'Client Type': Confidential,
    'Authorization grant type': Resource Owner password-based,
    'Redirect url': "",
    'Name': client_app,
}
```
Navigate to views.py file inside users app and replace the code with this:
```
CLIENT_ID = <Your Client ID>
CLIENT_SECRET = <Your Client Secret>
```
Now log out from admin page.

### Authentication and Token Access ###

Visit the url `http://localhost:8000/oauth/register/` and register using email,name and password.
Now visit the url `http://localhost:8000/oauth/token/` anf login to get the token.
Login credential should be of format : 
```
{
"email": "email@gmail.com",
"password": "email@123"
}
```
Once to login you will get response like:
```
{
    "access_token": "nHZ9xgZTaz1SDltTbxXUHjpVCmOAWp",
    "expires_in": 36000,
    "token_type": "Bearer",
    "scope": "read write",
    "refresh_token": "mbvjI8pbBPpG9FfyFyvLBQbMKgllUR"
}
```
Copy the access token and make an API request to a protected resource (A Todo API developed for this purpose at) using CURL or Postman
```
Todo List: `curl -H "Authorization: Bearer nHZ9xgZTaz1SDltTbxXUHjpVCmOAWp" http://localhost:8000/home/todo/`
Todo Create: `curl -H "Authorization: Bearer nHZ9xgZTaz1SDltTbxXUHjpVCmOAWp" -d "todo=test&done=True" http://localhost:8000/home/todo/`
```

### Running Test ###

`python manage.py test client_app.users.tests` 






