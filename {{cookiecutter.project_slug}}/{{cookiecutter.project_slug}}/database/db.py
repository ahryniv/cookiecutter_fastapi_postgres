from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

metadata = MetaData()
Base = declarative_base(metadata=metadata)
{{cookiecutter.project_prefix}}Session = sessionmaker(autocommit=False, autoflush=False)


def get_db():
    session = {{cookiecutter.project_prefix}}Session()
    try:
        yield session
    finally:
        session.close()
