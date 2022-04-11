import json
from typing import Any
import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta

Base: Any = declarative_base()

 
class Token(Base):
    __tablename__ = 'token'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(300))
    value = sa.Column(sa.Text)

    def __repr__(self) -> str:
        return self.name


class JsonValue(Base):
    __tablename__ = 'key_value'
    id = sa.Column(sa.Integer, primary_key=True)
    key = sa.Column(sa.String(300))
    data_str = sa.Column(sa.Text)

    def __repr__(self) -> str:
        return self.key

    @property
    def data(self):
        return json.loads(self.data_str)

    @data.setter
    def data(self, value) -> None:
        self.data_str = json.dumps(value)

    
   