import os
from pathlib import Path
import json

app_dir = Path(os.path.dirname(os.path.realpath(__file__)))
main_script_dir = app_dir.parent
models_folder = app_dir.parent / "models"
models_example_folder = app_dir / "models_example"
local_folder = app_dir.parent / ".local"
debug=False
try:
    local_folder.mkdir()
except FileExistsError:
    pass
workdir: Path = Path(".")
verbose = False
SECRET_KEY="!@#QWEsddda"

local_data_path = main_script_dir / "local_data.json"
try:
    with local_data_path.open("r", encoding="utf-8") as f:
        local_data = json.load(f)
except FileNotFoundError:
    local_data = {}