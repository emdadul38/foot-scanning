# foot-scanning

## Installation Instruction
1. Close the project 
```python
https://github.com/emdadul38/foot-scanning.git
```
2. cd into the project directory
```python
cd foot-scanning
```
3. Create a new virtual environment using Python 3.7 and activate it.
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
4. Install dependencies from requirements.txt;
```python
(venv)$ pip install -r requirements.txt
```
5. Migrate the database.

```python
(venv)$ cd foot-scanning
(venv)$ python manage.py migrate
```

6. Make admin user

```python
(venv)$ python manage.py createsuperuser
```

6. Run Server
```python
(venv)$ cd myproject
(venv)$ python manage.py runserver
```
## License
[MIT](https://choosealicense.com/licenses/mit/)
