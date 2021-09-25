from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

dbmetadata = MetaData()
BaseModel = declarative_base(metadata=dbmetadata)