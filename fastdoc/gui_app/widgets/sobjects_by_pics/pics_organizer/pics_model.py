from pathlib import Path
from PyQt5.QtCore import QAbstractListModel, Qt

class PicsModel(QAbstractListModel):
    def __init__(self, *args, pics=None, **kwargs):
        super(PicsModel, self).__init__(*args, **kwargs)
        self.pics: list[Path] = pics or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.pics[index.row()]

    def rowCount(self, index):
        return len(self.pics)