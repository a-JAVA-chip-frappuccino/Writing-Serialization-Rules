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

    serialize_rules = ('-manager.favorite_book', '-books_at_bookstore.book')

    uuid = db.Column(db.String, primary_key = True)
    name = db.Column(db.String)
    zip_code = db.Column(db.String)
    manager_uuid = db.Column(db.String, db.ForeignKey('managers.uuid'))

    manager = db.relationship('Manager', back_populates = 'bookstore')
    books_at_bookstore = db.relationship('BookAtBookstore', back_populates = 'bookstore')

class Manager(db.Model, SerializerMixin):
    __tablename__ = 'managers'

    serialize_rules = ('-favorite_book.biggest_fan', '-bookstore.manager')

    uuid = db.Column(db.String, primary_key = True)
    name = db.Column(db.String)
    favorite_book_isbn = db.Column(db.String, db.ForeignKey('books.isbn'))

    bookstore = db.relationship('Bookstore', back_populates = 'manager')
    favorite_book = db.relationship('Book', back_populates = 'biggest_fan')

class Book(db.Model, SerializerMixin):
    __tablename__ = 'books'

    serialize_rules = ('-biggest_fan.favorite_book', '-book_at_bookstores.book')

    isbn = db.Column(db.String, primary_key = True)
    title = db.Column(db.String)
    author_name = db.Column(db.String)
    page_count = db.Column(db.Integer)

    book_at_bookstores = db.relationship('BookAtBookstore', back_populates = 'book')
    biggest_fan = db.relationship('Manager', back_populates = 'favorite_book')

class BookAtBookstore(db.Model, SerializerMixin):
    __tablename__ = 'book_at_bookstore'

    serialize_rules = ('-book.book_at_bookstores', '-bookstore.books_at_bookstore', '-bookstore.manager')

    id = db.Column(db.Integer, primary_key = True)
    bookstore_uuid = db.Column(db.String, db.ForeignKey('bookstores.uuid'))
    book_isbn = db.Column(db.String, db.ForeignKey('books.isbn'))

    bookstore = db.relationship('Bookstore', back_populates = 'books_at_bookstore')
    book = db.relationship('Book', back_populates = 'book_at_bookstores')