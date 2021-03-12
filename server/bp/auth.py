# file for auth blueprint

import functools

from flask import (
    Blueprint, flash,
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET',))
def register():
    return {
        "data": "ok"
    }
