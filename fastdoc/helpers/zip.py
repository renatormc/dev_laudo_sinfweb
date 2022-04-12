from pathlib import Path
from typing import Optional, Union
import os
import zipfile

from setuptools import find_namespace_packages
from fastdoc import config
import shutil
from uuid import uuid4

def zip_folder(folder_path, output_path) -> None:
    contents = os.walk(folder_path)
    try:
        zip_file = zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED)
        for root, folders, files in contents:
            for folder_name in folders:
                absolute_path = os.path.join(root, folder_name)
                relative_path = absolute_path.replace(folder_path + os.sep, '')
                zip_file.write(absolute_path, relative_path)
            for file_name in files:
                absolute_path = os.path.join(root, file_name)
                relative_path = absolute_path.replace(folder_path + os.sep, '')

                zip_file.write(absolute_path, relative_path)
    finally:
        zip_file.close()

def unzip_file(file: Union[Path, str], dest: Optional[Union[Path, str]] = None, subfolder=False) -> Path:
    """Unzip a zip file to a folder. If dest is not especified it will be extracted to a temporary folder"""
    if dest is None:
        dest = config.TEMPFOLDER / str(uuid4())
    file, dest = Path(file), Path(dest)
    if dest.exists():
        shutil.rmtree(dest)
    if subfolder:
        dest = dest / file.name
    dest.mkdir(parents=True)

    with zipfile.ZipFile(str(file)) as zip_ref:
        zip_ref.extractall(str(dest))
    return dest
