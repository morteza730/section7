from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.stores import StoreModel


class Stores(Resource):
    @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"massage": "store not found"}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"massage": "store {} already exits.".format(name)}, 400
        store = StoreModel(name)
        try:
            store.save()
            return store.json()
        except:
            return {"massage": "inserting store {} was not successful".format(name)}, 500

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            try:
                store.delete()
                return {"massage": "deleting item {} was successful".format(name)}, 200
            except:
                return {"massage": "deleting item {} was not successful".format(name)}, 500
        else:
            return {"massage": "item {} doesn't exist in database"}


class StoreList(Resource):
    def get(self):
        return {"stores": [x.json() for x in StoreModel.query.all()]}
