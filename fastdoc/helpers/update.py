from pathlib import Path
from typing import TypedDict
import requests
import json
from fastdoc import config
import sys
import subprocess
import os


class ReleaseInfo(TypedDict):
    repo_url: str
    version: str

def get_local_version_info() -> ReleaseInfo:
    path = config.app_dir / "current_release.json"
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def get_remote_version_info() -> ReleaseInfo:
    r = requests.get("https://raw.githubusercontent.com/renatormc/fastdoc/master/fastdoc/current_release.json")
    if r.status_code == 200:
        data: ReleaseInfo = json.loads(r.text)
    else:
        return {'repo_url': '', 'version': ''}
    return data

def has_newer_version():
    info_remote = get_remote_version_info()
    info_local = get_local_version_info()
    return info_remote['version'] != info_local['version']

def update():
    if os.name == "nt":
        path = config.main_script_dir.parent / "fastdoc_updater/main.exe"
        subprocess.Popen(['cmd', '/k', str(path)])
        sys.exit()
