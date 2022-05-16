from pathlib import Path
from typing import Optional
from unicodedata import name

from sqlalchemy import JSON
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


def get_token(name: str) -> Optional[str]:
    token = db.session.query(Token).filter(Token.name == name).first()
    if token:
        return token.value
    return None


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


def delete_lists() -> None:
    db.session.query(ItemList).delete()
    db.session.commit()
    print("deletando listas")


def save_list(model_name: str, list_name: str, items: list[dict]) -> None:
    for item in items:
        item_list = ItemList()
        item_list.model_name = model_name
        item_list.list_name = list_name
        try:

            item_list.key = item['key']
            item_list.data = item['data']
            db.session.add(item_list)
        except KeyError:
            continue
    db.session.commit()


def get_list(model_name: str, list_name: str, filter: Optional[str] = None):
    query = db.session.query(ItemList).filter(
        ItemList.list_name == list_name,
        ItemList.model_name == model_name
    )
    if filter:
        query = query.filter(ItemList.key.ilike(f"%{filter}%"))
    return query.order_by(ItemList.key.asc()).all()


def save_last_data(model_name: str, data: Any) -> None:
    jvalue: JsonValue | None = db.session.query(JsonValue).filter(
        JsonValue.category == 'last_saved',
        JsonValue.key == model_name
    ).first()
    if not jvalue:
        jvalue = JsonValue()
        jvalue.category = 'last_saved'
        jvalue.key = model_name
    jvalue.data = data
    db.session.add(jvalue)
    db.session.commit()


def get_last_data(model_name: str) -> Any:
    jvalue: JsonValue | None = db.session.query(JsonValue).filter(
        JsonValue.category == 'last_saved',
        JsonValue.key == model_name
    ).first()
    return jvalue.data if jvalue else {}
