# FlatMX

Django 3.0 WebApp wrapper for git projects.


#Modules:

- authors
- branches
- commits
- pullrequests

#Requeriments:

- Python 3.8(Last version)

Before running please follow this steps:

- 1- Create new folder
- 2- Clone this repository and move the unzipped folder to new folder created previously
- 3- Open your terminal and move it to the path folder created on step 1
- 4- Create a virtual environment using the next command(MacOS):
```
                            python3 -m venv <yourvenvname>
```    

#Running local FlatMX webapp  

- 1- Open your cloned repository (located in your new folder created previously) using
your code editor preference (PyCharm, VisualStudioCode, ...)
- 2- Open your code editor's terminal and use "cd .." command to move one step back into directory path
- 3- Activate your virtual environment using the next command(MacOS):
```
                            source <yourvenvname>/bin/activate
```
- 4- Once you have activated your virtual environment return to your cloned repository one step forward using "cd" command 
- 5- Install all requirements located in requirements.txt file using the next command:
```
                            pip install -r requirements.txt
```
- 6- Done!!! You can run your local server using the nex command (MacOS):
```
                            python3 manage.py runserver
```
- 7- Open your browser at **127.0.0.1:8000**




#Unit Test Cases Location

- FlatMX/core/tests.py

#Running unit tests cases
- On your code editor's terminal type the nex command:
```
                            pytest core/tests.py
```

#Accessing to Admin Module
 If you want to access to admin module create a superuser following the next steps:
- On your code editor's terminal type the nex command(MacOS) and follow the prompt instructions:
```
                            python3 manage.py createsuperuser
```
Once you have created a superuser go to the next url and access with your superuser credentials
- **http://127.0.0.1:8000/admin/**
Now you can access to admin module's dashboard

#Local API Rest urls
- **http://127.0.0.1:8000/api/v1/authors/**
- **http://127.0.0.1:8000/api/v1/branches/**
- **http://127.0.0.1:8000/api/v1/commits/**
- **http://127.0.0.1:8000/api/v1/pulls/**

#Documentation url
- **http://127.0.0.1:8000/docs/**

#Admin url
- **http://127.0.0.1:8000/admin/**

#Bonus
- Unit Tests
- Documentation
