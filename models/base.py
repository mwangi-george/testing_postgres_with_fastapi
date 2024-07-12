from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from app.config import Config

Base = declarative_base()
config = Config()


# "postgresql://localhost/mydb?user=other&password=secret"
DATABASE_URL = f"postgresql://{config.DB_HOST}/{
    config.DB_NAME}?user={config.DB_USERNAME}&password={config.DB_PASSWORD}"


engine = create_engine(url=DATABASE_URL)


def recreate_postgres_tables():
    Base.metadata.create_all(engine)
