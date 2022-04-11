from fastdoc import config
from .db import DB

db = DB(config.DATABASE_URI)