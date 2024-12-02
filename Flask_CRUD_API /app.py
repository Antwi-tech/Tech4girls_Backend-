# This file uses endpoints to perform CRUD operations using GET,POST, PATCH PUT UPDATE to interact 
# with the databse

from laptops_blueprint import *
from flask import Flask, jsonify, request

app = Flask(__name__)
app.register_blueprint(laptop_device)

@app.route('/')
def home():
    return "Welcome to Flask"

if __name__ == '__main__':
    app.run(debug=True)
