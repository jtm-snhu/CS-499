# Rescue Animal Inventory Navigator

This application was built using Python 3.11.9 (Anaconda).
It requires SQLite on the host system.

You will also need to install the following modules in your environment for proper functioning.

flask  
flask-login  
flask-paginate  
flask-sqlalchemy  
flask-wtf  
email-validator

Try:

pip install flask flask-login flask-paginate flask-sqlalchemy flask-wtf email-validator

Or if you use an Anaconda distribution of Python:

conda install flask flask-login flask-paginate flask-sqlalchemy flask-wtf email-validator

With the necessary modules installed, at a terminal, switch into the app-python directory and enter:  
flask --debug run

You should then be able to see the application in your web browser by going to http://127.0.0.1:5000/

With a new intallation, the database and demo data will be created automatically. Click the signup link to create a user, then log in using those credentials to explore the application.