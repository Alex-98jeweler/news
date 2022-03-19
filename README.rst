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


On this stage you should get a following structure:

* news
    * env
    * news
    * test_task
    * Makefile
    * manage.py
    * README.rst
    * requirements.txt

Build
======

The content of this application have to be stored somewhere. Its storage is tables, which have to be created in a Database. Let's make migrations. The Django Framework(*it was installed on Virtual Environment stage*), does it automatically. For it, run command:

.. code-block::

    make migrations

This command prepares migrations and make them. In result, necessary tables are created into Database and you can show follow message:

.. code-block::

    python3 manage.py makemigrations news
    Migrations for 'news':
    news/migrations/0001_initial.py
        - Create model News
    python3 manage.py migrate
    Operations to perform:
    Apply all migrations: admin, auth, contenttypes, news, sessions
    Running migrations:
    Applying contenttypes.0001_initial... OK
    Applying auth.0001_initial... OK
    Applying admin.0001_initial... OK
    Applying admin.0002_logentry_remove_auto_add... OK
    Applying admin.0003_logentry_add_action_flag_choices... OK
    Applying contenttypes.0002_remove_content_type_name... OK
    Applying auth.0002_alter_permission_name_max_length... OK
    Applying auth.0003_alter_user_email_max_length... OK
    Applying auth.0004_alter_user_username_opts... OK
    Applying auth.0005_alter_user_last_login_null... OK
    Applying auth.0006_require_contenttypes_0002... OK
    Applying auth.0007_alter_validators_add_error_messages... OK
    Applying auth.0008_alter_user_username_max_length... OK
    Applying auth.0009_alter_user_last_name_max_length... OK
    Applying auth.0010_alter_group_name_max_length... OK
    Applying auth.0011_update_proxy_permissions... OK
    Applying auth.0012_alter_user_first_name_max_length... OK
    Applying news.0001_initial... OK
    Applying sessions.0001_initial... OK

The directory *migrations* have to be appear in *news/news/* directory.

Using
======

Finnaly, run: 

.. code-block::

    make run

If you see the following message, you've done it! Congratulations!
Body of message:

.. code-block::

    python3 manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).
    March 19, 2022 - 12:48:42
    Django version 4.0.3, using settings 'test_task.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

Now, follow the link http://127.0.0.1:8000/, and try to use this application. 


A page of news list look like:

* Without some data

    .. figure:: image/1.png
        :scale: 100%

* With some data. A count of items and pagination.

    .. figure :: image/3.png
        :scale: 100%

    .. figure :: image/4.png
        :scale: 100%

    .. figure :: image/5.png
        :scale: 100%

    .. figure :: image/6.png
        :scale: 100%

    .. figure :: image/7.png
        :scale: 100%

    .. figure :: image/8.png
        :scale: 100%

    .. figure :: image/9.png
        :scale: 100%

News create form: 

    .. figure :: image/2.png
        :scale: 100%

News detail information:

    .. figure :: image/10.png
        :scale: 100%

News delete:
    .. figure :: image/11.png
        :scale: 100%


    

