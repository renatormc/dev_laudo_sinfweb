from fastdoc.custom_types import ModelInfo
from fastdoc.helpers import get_models_info
from fastdoc import config
from database import repo
import json

def fix_model_lists(mi: ModelInfo):
    folder = config.models_folder / mi.name
    path = folder / "lists"
    if not path.exists() or not path.is_dir():
        path.mkdir()

def update_lists_to_db(mi: ModelInfo):
    print(f"Updating lists of model \"{mi.name}\"")
    folder = config.models_folder / mi.name
    path = folder / "lists"
    if path.exists() and path.is_dir():
        for entry in path.iterdir():
            if entry.is_file() and entry.suffix == ".txt":
                text = entry.read_text(encoding="utf-8")
                items: list[dict] = [{'key': line, 'data': line} for line in text.split("\n")]
                repo.save_list(mi.name, entry.stem, items)
            elif entry.is_file() and entry.suffix == ".json":
                with entry.open("r", encoding="utf-8") as f:
                    items = json.load(f)
                repo.save_list(mi.name, entry.stem, items)
                

def fix_old_models():
    mis = get_models_info()
    repo.delete_lists()
    for mi in mis:
        fix_model_lists(mi)
        update_lists_to_db(mi)