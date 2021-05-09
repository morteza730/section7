import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authentication, identify
from resourses.User import UserRegister
from resourses.items import Item, ItemList
from resourses.stores import Stores, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://sqwjfwhvaczgeu" \
                                        ":5741a1980d0229d3d1c311bdaa42eab6920409e6c9a391e78ad0f3f5fcb16871@ec2-54-164" \
                                        "-22-242.compute-1.amazonaws.com:5432/d396up6h1c6v6u"#os.environ.get(
# 'DATABASE_URL')#, 'sqlite:///data.db'
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
