from pathlib import Path
from fastdoc import config


class ObjectType:
    def __init__(self, folder: Path, type: str = "", pics: list[str] = [], name: str = "Sem nome") -> None:
        self.folder: Path = folder
        self.type: str = type
        self.pics: list[str] = pics
        self.name: str = name

    def pics_iterator(self):
        for pic in self.pics:
            yield self.folder / pic


class CaseObjectsType:
    def __init__(
            self, folder: Path = config.workdir, objects: list[ObjectType] = [],
            pics_not_classified: list[str] = [],
            alias: str = "") -> None:
        self.folder: Path = folder
        self.objects: list[ObjectType] = objects
        self.pics_not_classified: list[str] = pics_not_classified
        self.alias: str = alias

    def pics_not_classified_iterator(self):
        for pic in self.pics_not_classified:
            yield self.folder / pic
