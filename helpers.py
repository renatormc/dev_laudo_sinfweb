import models
import inquirer
import config



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
