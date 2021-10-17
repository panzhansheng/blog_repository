from sqlalchemy import Column
from sqlalchemy.types import String, Integer
from sqlalchemy.orm import relationship
from models import BaseModel 

class User(BaseModel):
    __tablename__ = 'user'
    public_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    password = Column(String(255))
    token = Column(String(255))

    fk_blog = relationship('Blog',back_populates="fk_blog_user", cascade="all, delete")

    def __repr__(self):
        return "<Blog(id='%s', name='%s', password='%s', token='%s'>" % (
                                self.public_id, self.name, self.password, self.token)
    def to_json(self):
        return ["id:",self.public_id,"name:", self.name, "password:", self.password, "token:", self.token ]

"""
class User (Base):
    __tablename__ = "User"
    id = Column('id', Integer, primary_key = True)
    name = Column('name', Unicode)
    password = Column('password', Unicode)
    token = Column('token', Unicode)

class Blog (Base):
    __tablename__ = "Blog"
    id = Column('id', Integer, primary_key = True)
    date = Column('date', Date)
    name = Column('name', Unicode)
    text = Column('text', Unicode)
    user_id = Column('User_id', Integer, ForeignKey('User.id'))

    user = relationship('User', foreign_keys=user_id)

"""