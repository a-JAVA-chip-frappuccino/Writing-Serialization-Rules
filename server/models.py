from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata = metadata)

class Bookstore(db.Model, SerializerMixin):
    __tablename__ = 'bookstores'

    uuid = db.Column(db.String, primary_key = True)
    name = db.Column(db.String)
    zip_code = db.Column(db.String)
    manager_uuid = db.Column(db.String, db.ForeignKey('managers.uuid'))

class Manager(db.Model, SerializerMixin):
    __tablename__ = 'managers'

    uuid = db.Column(db.String, primary_key = True)
    name = db.Column(db.String)
    favorite_book_isbn = db.Column(db.String, db.ForeignKey('books.isbn'))

class Book(db.Model, SerializerMixin):
    __tablename__ = 'books'

    isbn = db.Column(db.String, primary_key = True)
    title = db.Column(db.String)
    author_name = db.Column(db.String)
    page_count = db.Column(db.Integer)

class BookAtBookstore(db.Model, SerializerMixin):
    __tablename__ = 'book_at_bookstore'

    id = db.Column(db.Integer, primary_key = True)
    bookstore_uuid = db.Column(db.String, db.ForeignKey('bookstores.uuid'))
    book_isbn = db.Column(db.String, db.ForeignKey('books.isbn'))