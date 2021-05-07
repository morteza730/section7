from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.items import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price",
                        type=float,
                        required=True,
                        help='this field can not left blank')
    parser.add_argument("store_id",
                        type=int,
                        required=True,
                        help='every item needs a store id')

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"massage": "Item not found"}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"massage": "item {} already exits.".format(name)}, 400
        request_item_price = Item.parser.parse_args()
        item = ItemModel(name, **request_item_price)
        try:
            item.save()
            return item.json()
        except:
            return {"massage": "inserting item {} was not successful".format(name)}, 500

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            try:
                item.delete()
                return {"massage": "deleting item {} was successful".format(name)}, 200
            except:
                return {"massage": "deleting item {} was not successful".format(name)}, 500
        else:
            return {"massage": "item {} doesn't exist in database"}

    def put(self, name):
        request_item_price = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item:
            updated_item = ItemModel(name, **request_item_price)
            try:
                updated_item.save()
                return item.json()
            except:
                return {"massage": "updating item {} was not successful".format(name)}, 500
        else:
            try:
                item = ItemModel(name, **request_item_price)
                item.save()
                return item.json()
            except:
                return {"massage": "inserting item {} was not successful".format(name)}, 500


class ItemList(Resource):
    def get(self):
        return {"items": [x.json() for x in ItemModel.query.all()]}
