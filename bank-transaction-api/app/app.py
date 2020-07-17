from flask import Flask,jsonify,request
from flask_restful import Api, Resource

from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)


# create a new bank account user 
class Register(Resource):
    def post(self):
        postedData = request.get_json()


# deposit moneh into the account
class Add(Resource):
    def post(self):
        postedData = request.get_json()


# transfer money from one account to another
class Transfer(Resource):
    pass


# check the balance of an account
# should be a get request 
class CheckBalance(Resource):
    pass

class TakeLoan(Resource):
    pass

class PayLoan(Resource):
    pass





@app.route('/')
def hello():
    return "Hello world!"

api.add_resource(Register,'register')

if __name__ == "__main__":
    app.run('0.0.0.0')