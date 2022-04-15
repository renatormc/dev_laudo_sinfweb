from pathlib import Path 
import shutil

def copy_item(from_: Path, to: Path):
    if from_.is_dir():
        try:
            shutil.rmtree(to)
        except FileNotFoundError:
            pass
        shutil.copytree(from_, to)
    else:
        try:
           to.unlink()
        except FileNotFoundError:
            pass
        shutil.copy(from_, to)