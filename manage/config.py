from pathlib import Path
import os

script_dir = Path(os.path.dirname(os.path.realpath(__file__))).absolute()
app_dir = script_dir.parent
verbose = False