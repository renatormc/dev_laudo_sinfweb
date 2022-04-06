import re
from datetime import timedelta
from math import log2
import humanfriendly

def convert_to_bytes(value):
    value = value.replace(",", ".").replace(" ", "")

    res = re.search(r'([\d\.,]+)(.*)', value)
    text = res.group(1)
    number = float(text)
    unity = res.group(2).upper()
    if unity == 'B':
        return number
    elif unity == 'KB':
        return 1024*number
    elif unity == 'MB':
        return 1048576*number
    elif unity == 'GB':
        return 1073741824*number
    elif unity == 'TB':
        return 1099511627776*number
    elif unity == "PB":
        return 1125899906842624*number
    elif unity == "EB":
        return 1152921504606847000*number
    else:
        raise ValueError("Unity unknow")


def str2timedelta(value):
    parts = value.split(":")
    delta = timedelta(hours=int(parts[0]), minutes=int(
        parts[1]), seconds=int(parts[2]))
    return delta


def filesize2human(size):
    if not size:
        return
    _suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']

    order = int(log2(size) / 10) if size else 0
    return '{:.4g}{}'.format(size / (1 << (order * 10)), _suffixes[order]).replace(".", ",")


def parse_filesize(value):
    value = value.replace(",", ".")
    try:
        number = float(value)
        value = f"{number} GB"
    except ValueError:
        pass
    return humanfriendly.parse_size(value, binary=True)

def format_size(value):
    return humanfriendly.format_size(value, binary=True).replace(".", ",")

def add_render_kw(kargs, key, value):
    try:
        kargs['render_kw'][key] = value
    except KeyError:
        kargs['render_kw'] = {key: value}

def add_validators(kargs, validators: list):
    try:
        kargs['validators'] += validators
    except KeyError:
        kargs['validators'] = validators