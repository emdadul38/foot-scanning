# foot-scanning

## Make Virtualenv
On Linux:
```python
$ Python -m venv projectven
$ . venv/bin/activate
```

On Windows:
```python
> Python -m venv projectven
> venv/Scripts/activate
```

```python
(venv)$ pip install -r requirements.txt
```
## Migrate

```python
(venv)$ cd foot-scanning
(venv)$ python manage.py migrate
```

## Make admin user

```python
(venv)$ python manage.py createsuperuser
```

## Run Server
```python
(venv)$ cd myproject
(venv)$ python manage.py runserver
```
