# Troject
A simple to do list web app

## About

This is a simple to do list web app develped by [django framework](https://github.com/django/django) for the back-end part and [bootstrap 3.3.7](https://github.com/twbs/bootstrap) for its front-end.
Only superusers can add tasks to the app.

**Features:**
- To use the app login is needed.
- Each task is assigned to a user and it belongs to a single group.
- Tasks can be visited by only the superusers or by the user which the task is assigned to.
- Tasks can be deleted only if they are pending.
- A task can be done only by the superusers or by the user which the task is assigned to.
- Adding users is possible in the django's default admin panel by the superuser.
- Changing background and saving it in the cookies.

## How to start

To start the project you have to have python3 installed on your machine.

First create a virtual environment:

`virtualenv myenv`

activate it and then install the packages in the `requirements.txt` file:

`pip3 install -r requirements.txt`

run the server on your localhost:

`python3 manage.py runserver`

and open your browser go to [localhost:8000](http://localhost:8000/)

there are two users defined to test the project:

> **superuser**  
> _username:_ `alistvt`   
> _password:_ `nothackable`

> _username:_ `mrunknown`   
> _password:_ `nothackable`

**Tips**: To create new users or change the passwords enter the [admin page](http://localhost:8000/admin/) by the superuser credentials.


_Star this if you enjoyed :)_
