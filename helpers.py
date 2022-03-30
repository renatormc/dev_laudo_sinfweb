import subprocess
import os
from pathlib import Path
from typing import Union
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


def render_doc(model: str, context, file_: Union[Path, str, None] = None):
    path = Path(file_) if file_ is not None else config.app_dir / "compilado.docx"
    r = Renderer(model, config.app_dir / "models")
    p = r.render("", context, only_laudo=True)
    shutil.move(p, path)

def open_doc(file_: Union[str, Path]) -> None:
    if os.name == "nt":
        subprocess.Popen(['start', str(file_)], shell=True)
