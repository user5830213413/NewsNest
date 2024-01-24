from flask import Flask, session
from flask_cors import CORS
from flask_restful import Api

from models.db import db
from config import Config

app = Flask(__name__)
api = Api(app)
app.config.from_object(Config)
CORS(app)
db.init_app(app)

with app.app_context():
    db.create_all()


from resources import (
    NewsResource,
    NewsListResource,
    MyNewsList,
    LoginResource
)

api.add_resource(NewsListResource, '/api/news')
api.add_resource(LoginResource, '/api/login')
api.add_resource(NewsResource, '/api/news/<string:news_id>')
api.add_resource(MyNewsList, '/api/my-news')



if __name__ == "__main__":
    app.run(debug=True)