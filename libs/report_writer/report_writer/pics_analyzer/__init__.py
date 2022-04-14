import re
from typing import TypedDict, Optional


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
