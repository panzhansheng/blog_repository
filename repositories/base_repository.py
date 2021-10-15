class BaseRepository(object):
    def get(self, **pk):
        raise NotImplementedError()


    def get2(self, **pk):
        raise NotImplementedError()
    
    def find(self, **keys):
        raise NotImplementedError()

    def find2(self, **keys):
        raise NotImplementedError()
    
    
    def persist(self, entity):
        raise NotImplementedError()
    
    def delete(self, entity):
        raise NotImplementedError()
    
    def create(self, **kw):
        raise NotImplementedError()

    def all(self):
        raise NotImplementedError()

class FSQLAlchemyRepository(BaseRepository):

    def __init__(self, model, session):
        self.model = model
        self.session = session
    
    def persist(self, entity):
        self.session.add(entity)
        self.session.commit()
    
    def delete(self, entity):
        self.session.delete(entity)
        self.session.commit()
    
    def get(self, **pk):
        return self.session.query(self.model).filter_by(**pk).one()


    def get2(self, **pk):
        return self.session.query(self.model).filter(**pk).one()
    
    def find(self, **keys):
        return self.session.query(self.model).filter_by(**keys).all()
    

    def find2(self, **keys):
        return self.session.query(self.model).filter(**keys).all()
    
    
    def create(self, **kw):
        return self.model(**kw)

    def all(self):
        return list(self.session.query(self.model).all())
    # entity is an FSQLAlchemyRepository object to be updated    
    def update_pass(self, entity, new_pass):
        self.session.query(self.model).filter_by(public_id = entity.public_id).update({"password": new_pass})
        self.session.commit()
        # users = self.session.query(self.model).filter_by(public_id=entity.public_id).all()
        # users[0].name= entity.name
        # users[0].password = entity.password
        # return users[0]
