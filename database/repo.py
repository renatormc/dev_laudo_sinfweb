from typing import Optional
from database import db 
from database.models import *

def save_token(name: str, value: str) -> None:
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