# Lab: 33 - Authentication & Production Server
# Lab: 32 - Permissions & Postgresql
# Lab: 31 - Django REST Framework / Docker

---

### Project: Drums
### Author: Alejandro Rivera

---

Django project that builds an api application for drums.

* v1.2
  * Django REST Framework:
    * Adds JSON Web Token (JWT) authentication to the API. 
    * Keeps pre-existing authentication so the DRF browsable API still usable.
  * Docker:
    * Implements Gunicorn instead of Django’s built-in development server.
    * Implements Whitenoise to handle styling issues after switching over to Gunicorn.
    * Ensures data is persistent.
* v1.1
  * Django REST Framework: 
    * Adjusts project’s permissions so that only authenticated users have access to API.
    * Adds a custom permission so that only appropriate users can update or delete it.
    * Adds ability to switch user’s directly from browsable API.
  * Docker:
    * Updates `Dockerfile` based off `python:3.10-slim`.
    * Updates `docker-compose.yml` to run Django app as a web service. 
    * Adds `postgres` as a service.
* v1.0 
  * Implements the Django REST Framework.
  * Creates a database of drums 
  * Adds full CRUD functionality.
  * Allows user to Create, Read, Update and Delete "drums" directly in the api.
  * Implements Docker containers.
  * Creates an `.env` file 

### Setup

* Install dependencies in a `venv`
  * **run:** pip install -r requirements.txt
* Dependencies: 
  * [requirements.txt](requirements.txt)
* Update `.env` file with secret key 

### How to initialize/run your application

* Initialize server:
  * **run:** docker-compose up --build

### Links and Resources

* api page: 
  * Mac: [http://0.0.0.0:8000/api/v1/drums/](http://0.0.0.0:8000/api/v1/drums/)
  * Windows: [http://localhost:8000/api/v1/drums/](http://localhost:8000/api/v1/drums/) 
* admin page: 
  * Mac: [http://0.0.0.0:8000/admin/](http://0.0.0.0:8000/admin/)
  * Windows: [http://localhost:8000/admin/](http://localhost:8000/admin/)
    * username: admin
    * password: admin

### Tests

* [httpie](https://httpie.io/) must be installed:

  * Grab API data: 
    * http GET localhost:8000/api/v1/drums/
  * Obtain token:
    * http POST :8000/api/token/ username=admin password=admin
  * Grab API data with access token:
    * http :8000/api/v1/drums/ 'Authorization: Bearer ***access token here***'
  * Refresh token:
    * http POST :8000/api/token/refresh/ refresh=***refresh token here*** 


* **run:** python3 manage.py test