# ITech

## Communication channels
Reporting issues for bugs: [Link](https://github.com/mspj/ITech/issues)

Trello for todo list and progress: [Link](https://trello.com/b/IXdehIOW)

## How to
### Instructions for assessors
Please make sure you have virtual environment installed and currently in it. Then follow the instructions that match your operating system and run the server.

#### For *nix and OS X
```
$ make deploy
```

#### For Windows
```
$ pip install -r requirements.txt
$ python manage.py migrate
$ python populate_data.py
```

#### Run the application
```
$ python manage.py runserver
```

### To deploy
```
$ make        # pull new commits
$ make clean  # clear db, install dependencies, make migrations, migrate, and populate data
$ make deploy # pull new commits, clear db, install dependencies, make migrations, migrate, and populate data
```

### Creating tables in embedded database
`$ python manage.py migrate`

### Populating embedded database
`$ python populate_data.py`

## Documentations
Django 1.7: [Link](https://docs.djangoproject.com/en/1.7/)

Goodreads API: [Link](https://www.goodreads.com/api)

Foundation: [Link](http://foundation.zurb.com/sites/docs/)

jQuery: [Link](http://api.jquery.com/)
