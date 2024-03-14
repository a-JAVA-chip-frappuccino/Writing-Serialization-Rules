from app import app
from models import db, Bookstore, Manager, Book, BookAtBookstore

if __name__ == '__main__':
    with app.app_context():

        # clear tables of current data
        print("Clearing all tables...")

        Book.query.delete()
        BookAtBookstore.query.delete()
        Manager.query.delete()
        Bookstore.query.delete()

        print("Seeding books table...")

        books = [
            Book (
                isbn = '1',
                title = 'abc',
                author_name = 'abc abc',
                page_count = 1
            ),
            Book (
                isbn = '2',
                title = 'abc',
                author_name = 'abc abc',
                page_count = 1
            ),
            Book (
                isbn = '3',
                title = 'abc',
                author_name = 'abc abc',
                page_count = 1
            )
        ]

        db.session.add_all(books)

        print("Seeding managers table...")

        managers = [
            Manager (
                uuid = '1',
                name = 'abc abc',
                favorite_book_isbn = '2'
            ),
            Manager (
                uuid = '2',
                name = 'abc abc',
                favorite_book_isbn = '3'
            )
        ]

        db.session.add_all(managers)

        print("Seeding bookstores table...")

        bookstore = Bookstore (
            uuid = '1',
            name = 'abc abc',
            zip_code = '12345',
            manager_uuid = '1'
        )

        db.session.add(bookstore)

        print("Seeding join table...")

        joins = [
            BookAtBookstore (
                id = 1,
                bookstore_uuid = '1',
                book_isbn = '1'
            ),
            BookAtBookstore (
                id = 2,
                bookstore_uuid = '1',
                book_isbn = '2'
            ),
            BookAtBookstore (
                id = 3,
                bookstore_uuid = '1',
                book_isbn = '3'
            )
        ]

        db.session.add_all(joins)

        db.session.commit()