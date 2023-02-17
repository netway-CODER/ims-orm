from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# database settings:
Engine = create_engine("sqlite+pysqlite:///db.sqlite3", echo=False)
Session = sessionmaker(Engine)