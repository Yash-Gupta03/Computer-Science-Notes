# Django -

## Interview Questions

### 1. What is Django ?

Open source web application framework for backend development.

### 2. Steps to create a django app ?

1. install django, check with <br>
   python -m django --version
2. create project using <br>
   django-admin startproject mysite.
3. Details of all the files in django <br>
   1. manage.py - cmd line utility that lets to interact with django project.
   2. **init**.py - Empty file that tells python to consider this directory as python package.
   3. settings.py - helps to configure python project.
   4. urls.py - url declaration of the project.
   5. asgi.py: An entry-point for ASGI-compatible web servers to serve your project.
   6. wsgi.py: An entry-point for WSGI-compatible web servers to serve your project.
4. cmd to run the project <br>
   python manage.py runserver
5. To create an app <br>
   python manage.py startapp app1
6. Create a url.py in app1 and then create views that can render the templates.

### 3. Project vs App in Django ?

A project is collection of configuration and apps for a website. apps are the web applications.

### 4. path() in django ?

path has 4 arguments, route, view, kwargs, name.

### 5.Role of migrate command ?

The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py

### 6. Models ?

Database layout, it contains all the fields that the db is storing.

### Static and Dynamic pages

For everyone static pages are same but dynamic pages are different for each user.

Urls
Views
Templates
