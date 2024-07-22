from typing import List

from fastapi import APIRouter
from fastapi import Depends
from app.db.config import get_db
from sqlalchemy.orm import Session
from app.schemas.schemas import BookSchema, BookSchemaCreate, BookSchemaUpdate, Response

from app.db import crud

router = APIRouter()


@router.get('/', response_model=Response[List[BookSchema]])
async def get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip, limit)
    books_schema = [BookSchema.model_validate(book) for book in books]
    response = Response[List[BookSchema]](
        status='Ok',
        code='200',
        message='Success fetch all books',
        result=books_schema
    )

    return response


@router.get('/{id}', response_model=Response[BookSchema])
async def get_book(id: int, db: Session = Depends(get_db)):
    try:
        book = crud.get_book_by_id(db, id)
        book_schema = BookSchema.model_validate(book)
        return Response[BookSchema](
            status='Ok',
            code='200',
            message='Success fetch book',
            result=book_schema
        )

    except Exception as e:
        return Response[None](
            status='bad',
            code='',
            message='the book gone wrong',
            result=None
        )


@router.post('/', response_model=Response[BookSchema])
async def create_book(request: BookSchemaCreate, db: Session = Depends(get_db)):
    book = crud.create_book(db, request)
    book_schema = BookSchema.model_validate(book)

    return Response[BookSchema](
        status='Ok',
        code='200',
        message='Book created successfully',
        result=book_schema
    )


@router.put('/{id}', response_model=Response[BookSchema])
async def update_book(id: int, request: BookSchemaUpdate, db: Session = Depends(get_db)):
    try:
        book = crud.update_book(db, id, request)
        book_schema = BookSchema.model_validate(book)
        return Response[BookSchema](
            status='Ok',
            code='200',
            message='Success update book',
            result=book_schema
        )

    except Exception as e:
        return Response[None](
            status='bad',
            code='',
            message='the updated gone wrond',
            result=None
        )


@router.delete('/{id}', response_model=Response[BookSchema])
async def delete_book(id: int, db: Session = Depends(get_db)):
    try:
        book = crud.remove_book(db, id)
        book_schema = BookSchema.model_validate(book)
        return Response[BookSchema](
            status='Ok',
            code='200',
            message='Book deleted successfully',
            result=book_schema
        )

    except Exception as e:
        return Response[None](
            status='bad',
            code='',
            message='the deleted gone wrong',
            result=None
        )
