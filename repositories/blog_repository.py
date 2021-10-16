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

    def find(self,**keys):
        blog = db.BlogSQL.find(**keys)
        return blog

    def create(self, entity):
        db.BlogSQL.persist(entity)

    def delete(self, entiry):
        db.BlogSQL.delete(entiry)
    
    def update_text(self, entity, new_text):
        db.BlogSQL.update_blog(entity, new_text)
