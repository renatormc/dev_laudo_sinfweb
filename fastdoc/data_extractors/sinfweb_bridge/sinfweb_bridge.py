from .requester import Requester
from fastdoc.data_extractors.sinfweb_bridge import config as cf

def get_pericia_data(rg: int, ano: int) -> dict:
    req = Requester()
    url = f"{cf.URL_SINFWEB}/dados-pericia/{rg}/{ano}"
    res = req.get(url)
    if res.status_code == 200:
        return res.json()
    return {}