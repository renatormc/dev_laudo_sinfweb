from fastdoc.app_flask.form_base import FormBase
import importlib
from uuid import uuid4
import socket

def get_web_form(model: str) -> FormBase:
    form_module = importlib.import_module(f"models.{model}.web_form")
    form:  FormBase = form_module.WebForm()
    # form.load_extra_validators()
    return form

def random_id():
    return str(uuid4())

def get_available_port():
    port = 5000
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1', port))
        if result == 0:
            port += 1
            continue
        return port