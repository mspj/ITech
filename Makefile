all: pull

pull:
	git pull

clean:
	rm db.sqlite3
	python manage.py migrate
	python populate_data.py

deploy: pull clean
