## Introduction
A django project for task management. User can register, log in, and create, update, and set deadlines.  

* There are 6 endpoints:


### Features
* Only Authenticated users can see, create, update, and search for the tasks.
* Session Authentication is used for the Authorization. 

### Installation Guide
* Clone the repo from [here](https://github.com/harsh10tech/task-management).
* Python is a must for the project, so install Python if not already there.


### Usage
* Run the project with `python manage.py runserver 8000`
* Connect to the API endpoints using Postman or thunder client (VScode) on port 8000. 


### API Endpoints
The base url for all API endpoints is: _`locahost:8000/`_ and [https://task-management-qhwg.onrender.com/](https://task-management-qhwg.onrender.com/)

| Sl No.| HTTP Verbs | Endpoints | Action | 
| --- | --- | --- | --- |
| 1. | POST | `/register/` | To sign up a new user account| 
| 2. | POST | `/login/` | To login an existing user.|
| 3. | POST | `/tasks/` | To add a new task|
| 4. | PUT or POST | `/update-task/<id>/` | To update a task |
| 5. | POST | `/delete-task/<id>/` | To delete a task |
| 6. | GET | `/logout/` | To logout of the current session |

### Technologies Used 
* Django, Django-rest_framework
* VS Code as a platfrom
