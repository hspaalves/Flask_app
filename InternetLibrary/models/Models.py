from . import db
from marshmallow import fields, Schema

author = db.Table('tags',
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True)
)


class BookModel(db.Model):

    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    summary = db.Column(db.String(30), nullable=False)

    author = db.relationship('Author', secondary=author, lazy='subquery',
                             backref=db.backref('Books', lazy=True))

    def __init__(self, data):
        self.name = data.get('name')
        self.summary = data.get('summary')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_books():
        return BookModel.query.all()

    @staticmethod
    def get_one_book(id):
        return BookModel.query.get(id)

    def __repr__(self):
        return '<id {}>'.format(self.id)


class AuthorModel(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, data):
        self.name = data.get('name')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_authors():
        return AuthorModel.query.all()

    @staticmethod
    def get_one_author(id):
        return AuthorModel.query.get(id)

    def __repr__(self):
        return '<id {}>'.format(self.id)
