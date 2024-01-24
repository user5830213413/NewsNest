from models.db import db
from uuid import uuid4

from datetime import datetime

class News(db.Model):
    __tablename__ = "news"

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())

    @classmethod
    def get_all_news(cls):
        return cls.query.all()
    
    @classmethod
    def get_new_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    @classmethod
    def get_new_by_user_id(cls, _user_id):
        return cls.query.filter_by(user_id=_user_id).first()
    
    @classmethod
    def get_new_by_user_id_all(cls, _user_id):
        return cls.query.filter_by(user_id=_user_id).all()
        

    def db_save(self):
        db.session.add(self)
        db.session.commit()

    def db_delele(self):
        db.session.delete(self)
        db.session.commit()