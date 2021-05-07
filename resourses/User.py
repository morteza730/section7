from flask_restful import Resource, reqparse
from models.User import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='this field can not left blank')
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='this field can not left blank')

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"massage": "this username already exist"}, 400
        user = UserModel(**data)
        user.save()
        return {"massage": "user created successfully"}, 201
