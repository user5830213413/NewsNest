from flask import request
from flask_restful import Resource, reqparse

from models.news import News
from datetime import datetime

news_parser = reqparse.RequestParser()
news_parser.add_argument('title', type=str)
news_parser.add_argument('content', type=str)
news_parser.add_argument('user_id', type=str)


class NewsListResource(Resource):
    def get(self):
        return [{'id': news.id, 'title': news.title, 'content': news.content, 'created': news.created_at.strftime("%Y-%m-%d %H:%M:%S")} for news in News.get_all_news()]


    def post(self):
        data = news_parser.parse_args()
        news = News(title=data['title'], content=data['content'], user_id=data['user_id'])
        news.db_save()

        return {'message': 'Новость успешно добавлена!'}, 201
    
class NewsResource(Resource):
    def get(self, news_id):
        news = News.get_new_by_id(news_id)
        if not news:
            return {'message': 'Новость не найдена!'}, 404

        return {'id': news.id, 'title': news.title, 'content': news.content, 'user_id': news.user_id, 'created': news.created_at.strftime("%Y-%m-%d %H:%M:%S")}
    
    def put(self, news_id):
        data = news_parser.parse_args()
        news = News.get_new_by_id(news_id)
        time = datetime.now()

        if not news:
            return {'message': 'Новость не найдена!'}, 404
        

        if data['user_id'] == news.user_id:
            news.title = data['title']
            news.content = data['content']
            news.created_at = time
            news.db_save()
            return {'message': 'Успешное изменение новости!'}, 200
        
        return {'message': 'что то пошло не так'}, 400
    
    def delete(self, news_id):
        news = News.get_new_by_id(news_id)
        
        if not news:
            return {'message': 'Новость не найдена!'}, 404
        news.db_delele()
        
        return {'message': 'Успешное удаление новости!'}, 200
    
class MyNewsList(Resource):
    def get(self):
        user_id = request.headers.get('Authorization').split(' ')[1]
        if not user_id:
            return {'message': 'Новость не найдена!'}, 404
        
        return [{'id': news.id, 'title': news.title, 'content': news.content, 'created': news.created_at.strftime("%Y-%m-%d %H:%M:%S")} for news in News.get_new_by_user_id_all(user_id)]