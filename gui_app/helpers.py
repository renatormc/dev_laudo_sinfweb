import config
from PyQt5.QtGui import QIcon

def get_icon(name):
    return QIcon(str(config.app_dir / "images" / name)) 