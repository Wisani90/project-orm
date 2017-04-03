Django ORM Framework
===================


Test ORM based application to showcase features  discussed in the ELEN4009 research project.

## Contact Management Application

This is a restful implementation of a contact management application to store contact details of people.

Contact detail holds basic contact details, physical address info and relation grouping to the app user.

## Environment setup

The application was build on a virtual environment, with a requirement file included to replicate the environment.

Refer to http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/ to setup virtualenv and virtualenvwrapper for both windows and unix.

#### inside the cloned root directory:
##### Create virtualenv:
mkvirtualenv myCircle
pip install -r requirements.txt
python manage.py test
python manage.py runserver localhost:8000

to run the restful application.

