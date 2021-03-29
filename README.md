# Allocation Proration
The web application is built on the Flask framework. 

### The top-level directory layout(simplified MVC architecture)

    .allocation_proration
    ├── log                   # store the input and output data as json files
    ├── templates             # front and web app index.html
    ├── __init__.py           # the main controller helping communication between frontend and backend
    ├── models.py             # backend calculation


## Run
install the dependencies:
```
$ pip install -r requirements.txt
```
run flask:
```
$ export FLASK_ENV=development
$ export FLASK_APP=allocation_proration
$ flask run
* Running on http://127.0.0.1:5000/
```
open browser:
```
http://127.0.0.1:5000/
```