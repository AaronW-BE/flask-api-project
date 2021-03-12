# init file for api resource init

from flask_restful import Api

from server.resources.book import BookList, Book


def init_resources(app):
    api = Api(app)

    api.add_resource(BookList, "/books")
    api.add_resource(Book, "/books/<book_id>")

