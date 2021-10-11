from flask import Blueprint, request

from common.response import APIResponse
from common.decorators import send_format
from .services import SignUp, Login

bp_auth = Blueprint('auth', __name__, url_prefix='/auth')


@bp_auth.route('/signup', methods=['POST'])
@send_format
def user_sign_up():
    data = request.get_json()
    service = SignUp(data)
    res = service.run()
    return APIResponse(res, 201)


@bp_auth.route('/login', methods=['POST'])
@send_format
def user_log_in():
    data = request.get_json()
    service = Login(data)
    res = service.run()
    return APIResponse(res)
