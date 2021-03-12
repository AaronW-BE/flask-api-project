from flask_restful import reqparse, abort, Api, Resource


class BookList(Resource):

    def __init__(self):
        pass

    def get(self):
        return [
            {
                "title": "game of throne",
            },
            {
                "title": "game of throne",
            }
        ]

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

