import os
from pathlib import Path

app_dir = Path(os.path.dirname(os.path.realpath(__file__)))
models_folder = app_dir / "models"
local_folder = app_dir / ".local"
try:
    local_folder.mkdir()
except FileExistsError:
    pass
