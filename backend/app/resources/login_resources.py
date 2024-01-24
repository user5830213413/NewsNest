from flask import session
from flask_restful import Resource

from models.news import News
from uuid import uuid4


class LoginResource(Resource):
    def post(self):
        user_id = str(uuid4())
        user_id_check_db = News.get_new_by_user_id(user_id)

        if user_id_check_db:
            return {'message': 'Извините что то пошло не так! попробуйте снова'}, 400

        return {'message': 'Регистрация прошла успешна', 'user_id': user_id}, 201