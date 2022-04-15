from datetime import datetime

def str2date(value: str) -> datetime:
    try:
        return datetime.strptime(value, "%d/%m/%Y")
    except:
        raise Exception(f"{value} não é uma data válida")