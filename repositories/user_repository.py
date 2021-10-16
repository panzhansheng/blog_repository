import inject
import typing
import db
from models.Users import Users
import sys
import os

# add package search path for current file dir
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
for p in sys.path:
    print(f'path={p}')


class UserRepository:

    def __init__(self):
        pass

    def all(self) -> typing.List[Users]:
        list= db.UserSQL.all()
        return list
    
    def find(self,**keys):
        user = db.UserSQL.find(**keys)
        return user

    def create(self, entity):
        db.UserSQL.persist(entity)

    def delete(self, entiry):
        db.UserSQL.delete(entiry)
    
    def update_pass(self, entity, new_pass):
        db.UserSQL.update_pass(entity, new_pass)