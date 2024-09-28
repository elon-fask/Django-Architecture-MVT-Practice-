# Project Description:
In this project, I created a user authentication system where the User model stored user information, the view handled login and logout functionality, and the template displayed the user profile page.

# SUMMARY:

This Django project implements a user authentication system with user registration, login, logout, and profile views. User details are stored in a database using the Django User model. The project follows the Model-View-Template (MVT) architecture to ensure separation of logic and UI, with secure authentication handling.

# STEPS:

Install Django and create a project.
Set up user authentication in settings.py.
Create User model to store user info.
Create views for login, logout, and profile.
Set up URLs for authentication routes.
Create HTML templates for login, profile, and logout.
Add logic to handle login and logout actions.
Set up Django messages for authentication feedback.
Ensure secure password storage with Django's hashing.
Implement the profile page to display user information.
Test authentication and user flows thoroughly.
Integrate CSRF tokens for form security.
Configure URLs and navigation in templates.
Deploy the project locally for testing.
Document project usage in README.md.

# STRUCTURE:

/auth_system/
    ├── auth_system/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── asgi.py
    ├── authentication/
    │   ├── __init__.py
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   └── forms.py
    ├── templates/
    │   ├── login.html
    │   ├── profile.html
    │   ├── base.html
    │   └── logout.html
    ├── manage.py
    └── README.md


