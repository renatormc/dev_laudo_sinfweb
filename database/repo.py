from pathlib import Path
from typing import Optional
from database import db
from database.models import *


def save_token(name: str, value: str) -> None:
    token = db.session.query(Token).filter(Token.name == name).first()
    if not token:
        token = Token()
    token.name = name
    token.value = value
    db.session.add(token)
    db.session.commit()


def get_token(name: str) -> Optional[Token]:
    return db.session.query(Token).filter(Token.name == name).first()


def get_json_value(key):
    jvalue = db.session.query(JsonValue).filter(JsonValue.name == key).first()
    if jvalue:
        return jvalue.data


def save_json_value(key, data):
    jvalue = JsonValue()
    jvalue.key = key
    jvalue.data = data
    db.session.add(jvalue)
    db.session.commit()


def clear_item_list():
    db.session.query(ItemList).delete()
    db.session.commit()


def add_items_list(model_name: str, list_name: str, items: list[str]) -> None:
    for item in items:
        it = ItemList()
        it.list_name = list_name
        it.model_name = model_name
        it.text = item
        db.session.add(it)
    db.session.commit()


def search_list_items(model_name: str, list_name: str, search_term: str, limit: Optional[int] = None) -> list[str]:
    query = db.session.query(ItemList).filter(
        ItemList.model_name == model_name,
        ItemList.list_name == list_name,
        ItemList.ilike(f"%{search_term}%")
    ).order_by(ItemList.text.asc())
    if limit:
        query = query.limit(limit)
    items = query.all()
    return [item.text for item in items] if items else []


def get_last_workdir() -> Path:
    jvalue = db.session.query(JsonValue).filter(
        JsonValue.key == "last_work_dir").first()
    if not jvalue:
        return Path(".").absolute()
    return Path(jvalue.data).absolute()


def save_last_workdir(value: str | Path) -> None:
    jvalue = db.session.query(JsonValue).filter(JsonValue.key == "last_work_dir").first()
    if not jvalue:
        jvalue = JsonValue()
        jvalue.key = "last_work_dir"
    jvalue.data = str(value)
    db.session.add(jvalue)
    db.session.commit()
