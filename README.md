# ITech

## Communication channels
Reporting issues for bugs: [Link](https://github.com/mspj/ITech/issues)

Trello for todo list and progress: [Link](https://trello.com/b/IXdehIOW)

## How to
### To deploy
```
$ make        # pull new commits
# make clean  # clear db, make migrations, migrate, and populate data
$ make deploy # pull new commits, clear db, make migrations, migrate, and populate data
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
