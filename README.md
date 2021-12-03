# gram-clone

## Author 
Built by: [Victoria Beryl](https://github.com/Victoria045)

# Description
This is a clone of the website for Instagram photo application.

#### Prerequisites 
* python3.6
* pip
* Django

# Setup and Installation
#### Cloning the repository
* Open Terminal:

        $ git clone https://github.com/Victoria045/gram-clone.git
        $ cd gram-clone
        $ code . or atom . based on your text editor 

* Navigate into the folder, install and activate virtual environment

        $ python -m venv virtual

        $ source virtual/bin/acivate

* Install all dependencies in requirements.txt

        $ pip install -r requirements.txt

#### Setup the Database
* Setup the database username, password, host

      $ python manage.py makemigrations 

* Run migrations

       $ python manage.py migrate

### Running the Application
* To run the application, open the cloned repo in terminal and run the following commands:

        $ python3 manage.py runserver

### Testing the Application       
* To run unittests for the class application and check if it functions well:

        $ python3 manage.py test gram

## Known Bugs
* No known bugs so far, incase a bug is spotted pull requests are allowed.


## Technologies Used
* markdown

* Django_Bootstrap4 - for bootstrap version 4

* Heroku - online deployment


## Support and contact details
Incase of any issues at hand, please email me at victoriaberyl45@gmail.com

### License
MIT License. 