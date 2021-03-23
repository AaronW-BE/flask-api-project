from server.utils.response import resp_success, resp_fail
from flask import (
    Blueprint, flash, request, jsonify
)
from server.models import (
    User, ProfileSchema
)

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('<username>/profile', methods=['GET'])
def get_user_profile(username):
    # 检测用户是否存在，暂不验证参数是否合法
    user = User.query.filter_by(username=username).first()
    if user is None:
        return resp_fail("用户不存在")

    # 返回个人信息
    profile = ProfileSchema().dump(user.profile)
    return resp_success(profile)
