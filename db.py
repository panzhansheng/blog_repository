from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

from models.blog import  Blog
from models.Users import Users
from repositories.base_repository import FSQLAlchemyRepository
from models import dbmetadata

engine = create_engine('mysql+pymysql://pzs:pzspzsPzs0!@192.168.4.36/blog?charset=utf8')
Session = sessionmaker(bind=engine)
session = Session()

#metadata = MetaData()
BlogSQL = FSQLAlchemyRepository(Blog , session)
UserSQL = FSQLAlchemyRepository(Users , session)

def init_db():
    dbmetadata.create_all(bind=engine)