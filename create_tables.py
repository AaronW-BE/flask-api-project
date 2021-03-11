from server import db, create_app
from server.models import *

db.create_all(app=create_app())

