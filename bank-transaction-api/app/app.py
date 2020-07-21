from flask import Flask,jsonify,request
from flask_restful import Api, Resource

from pymongo import MongoClient

import bcrypt


'''
preliminary stuff
'''
app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")

db = client.BankAPI
users = db['Users']

'''
functions
'''
def userExist(username):
    return users.find({"Username":username}[0]).count() != 0

def verifyPw(username,password):
    if userExist(username):

        hashedPw = users.find({'Username':username})[0]['Password'] 
        
    return hashedPw == bcrypt.hashpw(password.encode('utf8'),hashedPw)

def generateRes(status,message):
    return jsonify({
        "status":status,
        "message":message
    })







'''
resources
'''


# create a new bank account user 
class Register(Resource):
    def post(self):
        postedData = request.get_json()
        username = postedData['Username']
        password = postedData['Password']

        if userExist(username):
            return generateRes(301,"user already exists")


        # create hashed password
        hashedPw = bcrypt.hashpw(password.encode('utf8'),bcrypt.gensalt())

        # now store the data
        users.insert({
            'Username':username,
            'Password':hashedPw,
            'Own':0,
            'Debt':0
        })
        # return 200 ok and sign up message
        return generateRes(200,"you successfuly signed up for the API")

        


# deposit moneh into the account
class Add(Resource):
    def post(self):
        postedData = request.get_json()
        username = postedData['username']
        password = postedData['password']
        amount = postedData['amount']


# transfer money from one account to another
class Transfer(Resource):
    def post(self):
        postedData = request.get_json()
        username = postedData['username']
        password = postedData['password']
        to = postedData['to']
        amount = postedData['amount']


# check the balance of an account 
class CheckBalance(Resource):
    def post(self):
        postedData = request.get_json()
        username = postedData['username']
        password = postedData['password']

    

class TakeLoan(Resource):
    def post(self):
        postedData = request.get_json()
        username = postedData['username']
        password = postedData['password']
        amount = postedData['amount']

class PayLoan(Resource):
    def post(self):
        postedData = request.get_json()
        username = postedData['username']
        password = postedData['password']
        amount = postedData['amount']





@app.route('/')
def hello():
    return "Hello world!"

api.add_resource(Register,'register')
api.add_resource(Add,'/add')
api.add_resource(Transfer,'/transfer')
api.add_resource(CheckBalance,'/balance')
api.add_resource(TakeLoan,'/takeLoan')
api.add_resource(PayLoan,'/payLoan')

if __name__ == "__main__":
    app.run('0.0.0.0')