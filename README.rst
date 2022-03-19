Preparation
======================
Enter in the terminal following commands for creating a directory of an app:

.. code-block:: shell

    mkdir news
    cd news

Clone repo:

.. code-block::

    git clone git@github.com:Alex-98jeweler/news.git .


Database
---------
For beginning, you have to configure database. In the file *test_task2/test_task/settings.py* you can see a dict DATABASE, which looks like:

.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql', # PostgreSQL engine
            'NAME': 'news', # database name
            'USER': 'postgres', 
            'PASSWORD': 'postgres',
            'HOST' : 'localhost',
            'PORT': '5432'
        }
    }

If PostgreSQL is installed, no need to change this data, because user "postgres" with password "postgres" was created. Also no need to change 'HOST' and 'PORT'. All of this are default settings for PostgreSQL Database server.
Let's create new database. In your terminal enter command:

.. code-block::

    $su postgres

Terminal asks to enter password. Enter password "postgres". You switched on postgres user.
If you do right, you can see like:

.. code-block::

    postgres@LAPTOP:$

Further enter:

.. code-block::

    $ psql

Great, you are in PostgreSQL terminal and you can see:

.. code-block::

    postgres=#

Enter SQL query:

.. code-block::

    CREATE DATABASE news;

Congrate! You've created database and can continue preparation.
Now you have to create virtual environment and tables for this app.

Virtual Environment
-------------------

For successful running of a app, you have to create virtual environment and install some libraries, that are contained in the file *requirements.txt*. Run commands:

.. code-block::

    python3 -m venv env \
    source env/bin/activate \
    pip install -r requirements.txt


On this stage you should get such structure:

*news
    *env
    *news
    *test_task
    *Makefile
    *manage.py
    *README.rst
    *requirements.txt








    
    



    




