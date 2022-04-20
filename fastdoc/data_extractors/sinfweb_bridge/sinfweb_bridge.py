from .requester import Requester
from fastdoc.data_extractors.sinfweb_bridge import config as cf


class SinfwebBrigde:
    def __init__(self) -> None:
        self._data: dict = {}

    def get_pericia_data(self, rg: int, ano: int) -> None:
        req = Requester()
        url = f"{cf.URL_SINFWEB}/dados-pericia/{rg}/{ano}"
        res = req.get(url)
        if res.status_code == 200:
            self._data = res.json()

    def get_item(self, name):
        try:
            return self._data[name]
        except KeyError:
            return None

