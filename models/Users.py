from sqlalchemy import Column
from sqlalchemy.types import String, Integer
from sqlalchemy.orm import relationship
from models import BaseModel 

class Users(BaseModel):
    __tablename__ = 'users'
    public_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    password = Column(String(255))
    token = Column(String(255))

    def __repr__(self):
        return "<Blog(id='%s', name='%s', password='%s', token='%s'>" % (
                                self.public_id, self.name, self.password, self.token)
    def to_json(self):
        return ["id:",self.public_id,"name:", self.name, "password:", self.password, "token:", self.token ]