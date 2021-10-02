from sqlalchemy import Column
from sqlalchemy.types import String, Integer
from sqlalchemy.orm import relationship
from models import BaseModel 

class Blog(BaseModel):
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String(255))
    name = Column(String(255))
    text = Column(String(255))

    def __repr__(self):
        return "<Blog(id='%s', date='%s', name='%s', text='%s'>" % (
                                self.id, self.date, self.name, self.text)
    def to_json(self):
        return ["id:",self.id,"date:", self.date, "name:", self.name, "text:", self.text ]