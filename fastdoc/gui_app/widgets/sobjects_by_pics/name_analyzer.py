from pathlib import Path
import re
from typing import Optional, TypedDict, Union
from fastdoc.gui_app.widgets.types import ValidationError


class LaudoObject(TypedDict):
    number: str
    pics: list[str]


class LaudoObjects(TypedDict):
    alias: str
    objects: list[LaudoObject]


class AnalyzedPicInfo(TypedDict):
    obj_name: str
    alias: str
    obj_number: str
    pic_seq: str


class NameAnalyzer:
    def __init__(self):
        self.reg = re.compile(r'((^[A-Za-z]+)(\d+))(?:[\d\.\-]+)?(?:_(\d+))?$')

    def analise_name(self, name) -> Optional[AnalyzedPicInfo]:
        res = self.reg.search(name)
        if not res:
            return None
        ret: AnalyzedPicInfo = {
            'obj_name': res.group(1),
            'alias': res.group(2),
            'obj_number': res.group(3),
            'pic_seq': res.group(4)
        }
        if ret['obj_number'] is not None:
            return ret


def get_objects_from_pics(folder: Union[Path, str]) -> LaudoObjects:
    folder = Path(folder)
    objects: LaudoObjects = {'alias': '', 'objects': []}
    analyzer = NameAnalyzer()
    obj_map: dict[str, LaudoObject] = {}
    for entry in folder.iterdir():
        if entry.name.startswith("_"):
            continue
        res = analyzer.analise_name(entry.stem)
        if not res:
            continue
        if objects['alias'] and res['alias'] != objects['alias']:
            raise ValidationError("Encontradas fotos de mais de perícias diferentes dentro da pasta")
        objects['alias'] = res['alias']
        try:
            obj_map[res['obj_number']]['pics'].append(str(entry.absolute()))
        except KeyError:
            obj: LaudoObject = {
                'number': res['obj_number'],
                'pics': [str(entry.absolute())]
            }
            obj_map[res['obj_number']] = obj
    objects['objects'] = [obj for obj in obj_map.values()]
    return objects


