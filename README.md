# Streamline Patient Onboarding for Family Practices

## Problem Statement
Joining a new family practice often involves cumbersome paper forms and lengthy intake processes. This is a frustrating experience for patients and creates extra work for staff.

## Goal
Design and build a user-friendly web enrollment form that simplifies the patient onboarding process for family practices.

## Technologies Used 🛠️
- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
- ![Streamlit](https://img.shields.io/static/v1?style=for-the-badge&message=Streamlit&color=FF4B4B&logo=Streamlit&logoColor=FFFFFF&label=)
- ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
- ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
- ![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
- ![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
- ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
- ![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)


## Features
- User-friendly web form for patient enrollment.
- Capture all required patient information.
- Simple and intuitive user interface.
- Form validation to ensure data accuracy.
- Automatically generate a PDF document with submitted patient information.
- Online signature for signing the form (Bonus feature).

## Code Structure
myproject/                          -- Root directory of your Django project
- app_name/                         -- Django app folder (replace app_name with your app's name)
  - migrations/                     -- Database migrations (auto-generated by Django)
  - templates/                      --  HTML templates for the app
  - static/                         -- Static files (CSS, JavaScript, images)
  - __init__.py                     -- Initialization file (marks the directory as a Python package)
  - admin.py                        -- Register models for Django admin
  - apps.py                         -- App configuration
  - models.py                       -- Define Django models for patient information
  - forms.py                        -- Define forms for data input and validation
  - views.py                        -- Handle HTTP requests and form processing
  - urls.py                         -- Define URL patterns for the app
  - tests.py                        -- Optional: Unit tests for the app
- manage.py                         -- Django management script
- myproject/                        -- Project settings and configurations
  - __init__.py                     -- Initialization file (marks the directory as a Python package)
  - settings.py                     -- Django settings (database, static files, middleware, etc.)
  - urls.py                         -- Project-level URL patterns
  - asgi.py                         -- ASGI configuration for Django Channels (if used)
  - wsgi.py                         -- WSGI configuration for deployment
- static/                           -- Project-wide static files (CSS, JavaScript, images)
- templates/                        -- Project-wide HTML templates
  - base.html                       -- Base HTML template (common elements shared across pages)
- requirements.txt                  -- Python dependencies (generated using pip freeze > requirements.txt)
- README.md                         -- Project overview, instructions, and documentation

## Installation and Usage
1. Navigate to the project directory: `cd myproject`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the Django development server: `python manage.py runserver`
4. Access the web form in your browser at http://localhost:8000/

## Sample Filled Forms
- [Filled Sample Form 1](https://github.com/varshasenthil2003/Bewell_hackathon/blob/main/filled_form_S.pdf)
- ### Watch the Demo Video
[![MYSQL](https://img.youtube.com/vi/YOUR_VIDEO_ID_HERE/0.jpg)](https://github.com/varshasenthil2003/Bewell_hackathon/blob/main/mysql.mp4)
[![FORMS](https://img.youtube.com/vi/YOUR_VIDEO_ID_HERE/0.jpg)](https://github.com/varshasenthil2003/Bewell_hackathon/blob/main/forms.mp4)
[![RESULT](https://img.youtube.com/vi/YOUR_VIDEO_ID_HERE/0.jpg)](https://github.com/varshasenthil2003/Bewell_hackathon/blob/main/result(2).mp4)
