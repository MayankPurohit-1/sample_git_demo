from flask_restful import Resource
from flask import request
from Model.BaseModel import register_user


class UserRegister(Resource):
    def get(self):
        return "Enter the email and password"

    def post(self):
        data = request.get_json()
        if data:
            confirm = register_user(data['email'], data['password'])
            if confirm:
                return "Successful"



