from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp
# from flask_jwt_extended import (
#     create_access_token,
#     create_refresh_token,
#     jwt_refresh_token_required,
#     get_raw_jwt,
#     jwt_required
# )

from models.users import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('f_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('l_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    # parser.add_argument('has_partner',
    #                     type=str,
    #                     required=True,
    #                     help="This field cannot be left blank!"
    #                     )
    # parser.add_argument('partner_id',
    #                     type=str,
    #                     required=True,
    #                     help="This field cannot be left blank!"
    #                     )
    # parser.add_argument('pair_list',
    #                     type=str,
    #                     required=True,
    #                     help="This field cannot be left blank!"
    #                     )
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_email(data['email']):
            return {"message": "User with that email already exists."}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201

class User(Resource):
    @classmethod
    def get(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User not found.'}, 404
        return user.json()

    @classmethod 
    def delete(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User not found.'}, 404
        user.delete_from_db()
        return {'message': 'User deleted.'}, 200
