from flask import Flask
from flask_restful import Api
from Resource.User import UserRegister

app = Flask(__name__)
api = Api(app)


api.add_resource(UserRegister, '/register')


app.run(debug=True)
