from sqlalchemy.orm import Session

from app.models.models import Book
from app.schemas.schemas import BookSchemaCreate, BookSchemaUpdate


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()


def get_book_by_id(db: Session, id: int):
    book = db.query(Book).get(id)
    if book is None:
        raise Exception('Book not found')

    return db.query(Book).get(id)


def create_book(db: Session, book: BookSchemaCreate):
    book = Book(
        title=book.title,
        description=book.description,
    )

    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def update_book(db: Session, id: int, book_schema: BookSchemaUpdate):
    book = db.query(Book).get(id)
    if book is None:
        raise Exception('Book not found')

    book.title = book_schema.title
    book.description = book_schema.description
    db.commit()
    db.refresh(book)
    return book


def remove_book(db: Session, id: int):
    book = db.query(Book).get(id)
    if book is None:
        raise Exception('Book not found')

    db.delete(book)
    db.commit()
    return book
