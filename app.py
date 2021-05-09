import os
import re
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authentication, identify
from resourses.User import UserRegister
from resourses.items import Item, ItemList
from resourses.stores import Stores, StoreList

app = Flask(__name__)
uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
# 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "sadeghi"
jwt = JWT(app, authentication, identify)  # /auth
api = Api(app)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Stores, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
