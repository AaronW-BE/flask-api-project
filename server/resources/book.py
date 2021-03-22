from flask_restful import reqparse, abort, Api, Resource
from server.models import Book as BookModel
from server.models import BookSchema
from server.utils.response import resp_success, resp_paginate


class BookList(Resource):

    def __init__(self):
        pass

    def get(self):
        books = BookModel.query.paginate(page=1)
        books_schema = BookSchema(many=True)
        return resp_paginate(books, books_schema)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("title", required=True, help="title must be not empty")
        args = parser.parse_args()
        pass


class Book(Resource):
    def get(self, book_id):
        return {
            "id": book_id,
            "title": "game of throne",
        }

    def put(self, book_id):
        pass

    def delete(self, book_id):
        pass

