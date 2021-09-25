import inject
import typing
import db
from models.blog import Blog
import sys
sys.path.append('./')

class BlogRepository:

    def __init__(self):
        pass

    def all(self) -> typing.List[Blog]:
        list= db.BlogSQL.all()
        return list