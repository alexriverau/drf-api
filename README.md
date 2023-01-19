# Lab: 31 - Django REST Framework / Docker

---

### Project: Drums
### Author: Alejandro Rivera

---

Django project that builds an api application for drums.
 
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
  * **run:** docker-compose up

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

* **run:** python3 manage.py test