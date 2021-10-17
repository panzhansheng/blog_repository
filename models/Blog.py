from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.types import String, Integer
from sqlalchemy.orm import relationship
from models import BaseModel 

class Blog(BaseModel):
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String(255))
    name = Column(String(255))
    text = Column(String(255))

    # ForeignKey identify the user this blog belongs to. This is a 1-many relation
    # inside ForeignKey('user.public_id'), user.public_id is tablename_col_name, so must be lower case(not the Classname.attr)
    user_public_id = Column(Integer, ForeignKey('user.public_id'))
    # in relationship, parameter is the Class name, so must be uppercase(Object name) 
    fk_blog_user = relationship("User", foreign_keys=user_public_id, back_populates="fk_blog")

    def __repr__(self):
        return "<Blog(id='%s', date='%s', name='%s', text='%s'>" % (
                                self.id, self.date, self.name, self.text)
    def to_json(self):
        return ["id:",self.id,"date:", self.date, "name:", self.name, "text:", self.text ]

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