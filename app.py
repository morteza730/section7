from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authentication, identify
from resourses.User import UserRegister
from resourses.items import Item, ItemList
from resourses.stores import Stores, StoreList
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "sadeghi"
jwt = JWT(app, authentication, identify)  # /auth
api = Api(app)
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Stores, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)