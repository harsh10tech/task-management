## Introduction
A django project for doctors listing and to book appointments for patients. The system is for two kinds for user. For doctors and patients. Doctors can register, login and set there schedule accordigly. Patients can register, login, see all the available doctors based on location, specialization, and day of the week, and book an appointment also.

There are 7 endpoints:
* 3 for Doctors side
* 4 for Patient side

#### Watch the video demo [here](https://drive.google.com/file/d/1XsqvOv1S-7yjZhHjwlqHQSu--Py35LZe/view?usp=sharing)

### Features
* Only Authenticated users can set doctors' schedules, get the list of doctors, and book an appointment.
* Token Authentication is used for the Authorization. 

### Installation Guide
* Clone the repo from [here](https://github.com/harsh10tech/doctor-appointment.git).
* Python is a must for the project, so install Python if not already there.


### Usage
* Run the project with `python manage.py runserver 8000`
* Connect to the API endpoints using Postman or thunder client (VScode) on port 8000. 


### API Endpoints
The base url for all API endpoints is: _`locahost:8000/`_ and [http://harshcode2020.pythonanywhere.com](http://harshcode2020.pythonanywhere.com)

| Sl No.| HTTP Verbs | Endpoints | Action | 
| --- | --- | --- | --- |
| 1. | POST | `/doctorapi/doctor/signup/` | To sign up a new user account as a doctor| 
| 2. | POST | `/doctorapi/doctor/signin/` | To login an existing user account as a doctor. Returns a token. |
| 3. | POST | `/doctorapi/setdoc/setschedule/` | To create a new schedule or edit the existing one |
| 4. | POST | `/patientapi/patient/signup/` | To sign up a new user account as patient. |
| 5. | POST | `/patientapi/patient/signin/` | To login an existing user account as a patient. Returns a token. |
| 6. | POST | `/patientapi/appointment/bookappointment/` | To book an appointment. |
| 7. | GET | `/patientapi/appointment/getdoctors/` | To retrive all the doctors and their data for the current month.  |

### Technologies Used 
* Django, Django-rest_framework
* VS Code as a platfrom
