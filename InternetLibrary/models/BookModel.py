from . import db


class BookModel(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Interger)
    name = db
