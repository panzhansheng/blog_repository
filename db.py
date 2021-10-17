from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

from models.Blog import  Blog
from models.User import User
from repositories.base_repository import FSQLAlchemyRepository
from models import dbmetadata

engine = create_engine('mysql+pymysql://pzs:pzs@localhost/blog?charset=utf8')
Session = sessionmaker(bind=engine)
session = Session()

#metadata = MetaData()
BlogSQL = FSQLAlchemyRepository(Blog , session)
UserSQL = FSQLAlchemyRepository(User , session)

def init_db():
    dbmetadata.create_all(bind=engine)
