run:
	python3 manage.py runserver

migrations: 
	python3 manage.py makemigrations news
	python3 manage.py migrate

