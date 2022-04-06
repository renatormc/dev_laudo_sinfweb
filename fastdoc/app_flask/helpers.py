from fastdoc.app_flask.form_base import FormBase
import importlib

def get_web_form(model: str) -> FormBase:
    form_module = importlib.import_module(f"models.{model}.web_form")
    form:  FormBase = form_module.WebForm()
    # form.load_extra_validators()
    return form