from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from util.common import read_db_config

connection_string = "postgresql://zzidzz:lkjhgfdsaZXCVBNM1234567890@erp.postgres.database.azure.com/postgres"
engine = create_engine(connection_string, connect_args={'sslmode':'require'}, echo=True)
# use session_factory() to get a new Session
_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()


def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()