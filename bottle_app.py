# A very simple Bottle Hello World app for you to get started with...
import os
from bottle import default_app, run, route

@route('/')
def hello_world():
    return 'Hello from the sample repo app!'

if "PYTHONANYWHERE_DOMAIN" in os.environ:
    application = default_app()
else:
    run(host='localhost', port=8080)