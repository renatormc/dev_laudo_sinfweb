import models
import inquirer
import config
from report_writer import Renderer
import shutil


def get_test_context(model):
    mod = getattr(models, model)
    return mod.test_data.context


def get_models_list():
    models = []
    for entry in config.models_folder.iterdir():
        if entry.is_dir() and (entry / "templates").exists():
            models.append(entry.name)
    return models


def choose_model():
    questions = [
        inquirer.List('model', message="Escolha o modelo:", choices=get_models_list())
    ]
    answers = inquirer.prompt(questions)
    return answers['model']


def render_doc(model: str, context):
    r = Renderer(model, config.app_dir / "models")
    path = r.render("", context, only_laudo=True)
    shutil.move(path, config.app_dir / "compilado.docx")
