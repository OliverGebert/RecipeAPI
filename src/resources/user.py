from http import HTTPStatus

from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from models.user import User
from Utilities.utils import hash_password


class UserResource(Resource):
    @jwt_required(optional=True)
    def get(self, username):
        user = User.get_by_username(username=username)

        if user is None:
            return {"message": "user not found"}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()
        if current_user == user.id:
            data = {"id": user.id, "username": user.username, "email": user.email}
        else:
            data = {"id": user.id, "username": user.username}

        return data, HTTPStatus.OK


class UserListResource(Resource):
    def post(self):
        json_data = request.get_json()

        username = json_data.get("username")
        email = json_data.get("email")
        non_hash_password = json_data.get("password")

        if User.get_by_username(username):
            return {"message": "username already used"}, HTTPStatus.BAD_REQUEST

        if User.get_by_email(email):
            return {"message": "email already used"}, HTTPStatus.BAD_REQUEST

        password = hash_password(non_hash_password)
        user = User(username=username, email=email, password=password)
        user.save()
        data = {"id": user.id, "username": user.username, "email": user.email}

        return data, HTTPStatus.CREATED
