from flask import request, make_response

from config import app

from models import Book, BookAtBookstore, Manager, Bookstore

@app.route('/books', methods = ['GET'])
def books():
    books = Book.query.all()

    books_dict = [book.to_dict() for book in books]

    response = make_response(
        books_dict,
        200
    )

    return response

@app.route('/managers', methods = ['GET'])
def managers():
    managers = Manager.query.all()
    
    managers_dict = [manager.to_dict() for manager in managers]

    response = make_response(
        managers_dict,
        200
    )

    return response

@app.route('/bookstores', methods = ['GET'])
def bookstores():
    bookstores = Bookstore.query.all()
    
    bookstores_dict = [bookstore.to_dict() for bookstore in bookstores]

    response = make_response(
        bookstores_dict,
        200
    )

    return response

@app.route('/books_at_bookstores', methods = ['GET'])
def books_at_bookstores():
    books_at_bookstores = BookAtBookstore.query.all()
    
    books_at_bookstores_dict = [book_at_bookstore.to_dict() for book_at_bookstore in books_at_bookstores]

    response = make_response(
        books_at_bookstores_dict,
        200
    )

    return response

if __name__ == '__main__':
    app.run(port = 5555, debug = True)