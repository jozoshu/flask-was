from core.app import db
from common.exception import APIException
from common.response.client_error import Http4XX
from common.utils import hash_password, check_password
from .authentication import make_token
from .models import User


class SignUp:
    """회원가입 프로세스"""

    def __init__(self, data: dict):
        self.data = data

    def validate(self):
        try:
            assert self.data.get('phone_number')
            assert self.data.get('user_email')
            assert self.data.get('password')
            assert self.data.get('password2')
        except AssertionError as e:
            raise APIException(Http4XX.INVALID_PARAMS)

        if self.data.get('password') != self.data.get('password2'):
            raise APIException(Http4XX.WRONG_PASSWORD)

        user = User.query.filter_by(
            phone_number=self.data.get('phone_number')
        ).all()
        if len(user)>0:
            raise APIException(Http4XX.INVALID_PHONE_NUMBER, phone_number=self.data.get('phone_number'))


    def save(self):
        password = hash_password(self.data.get('password'))
        user = User(
            phone_number=self.data.get('phone_number'),
            user_email=self.data.get('user_email'),
            password=password,
        )
        db.session.add(user)
        db.session.commit()
        return user

    def run(self) -> dict:
        self.validate()
        user = self.save()
        return {
            'token': make_token(user)
        }


class Login:
    """로그인 프로세스"""

    def __init__(self, data: dict):
        self.data = data

    def validate(self):
        try:
            assert self.data.get('user_email')
            assert self.data.get('password')
        except AssertionError:
            raise APIException(Http4XX.INVALID_PARAMS)

    def get_user(self):
        users = User.query.filter_by(
            user_email=self.data.get('user_email')
        ).all()

        if len(users) == 0:
            raise APIException(Http4XX.WRONG_EMAIL, user_email=self.data.get('user_email'))

        if not check_password(self.data.get('password'), users[0].password):
            raise APIException(Http4XX.WRONG_PASSWORD)
        return users[0]

    def run(self) -> dict:
        self.validate()
        user = self.get_user()
        return {
            'token': make_token(user)
        }
