#Imports
from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from flask_swagger_ui import get_swaggerui_blueprint
import json
import random

# Create the application instance
app = Flask(__name__)

app_name = "API Demo"
api = Api(app)

# Swagger config
#
# This is the path to where you have your /static/swagger.json file
# Sample : https://github.comPrincekrampah
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': app_name
    }
)
app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

# Variables
playerList = []
todos = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

# Create a URL route in our application for "/"
@app.route('/', methods=['GET'])
def apiReady():
    return 'This ' + app_name + ' is ready !'

@app.route('/get-fruit', methods=['GET'])
def get_fruit():
    listFruits = ['apple', 'banana', 'orange', 'strawberry', 'grape', 'watermelon']
    choiseFruit = listFruits[random.randint(0, 2)]
    return json.dumps({'fruit': choiseFruit})

@app.route('/get/<name>/<years>', methods=['GET'])
def getInfo(name, years):
    return "Hello " + name + " you are " + years + " years old 👋"

@app.route('/add/', methods=['POST'])
def add():
    if request.method == 'POST':
        data = request.json
        playerList.append(data)
        print('[add-ok]'+data)
        return "created !"
    else:
        print('[add-error]'+data)
        return "Bad request", 400

#@app.route('add-player', methods=['POST'])
#def addPlayer():
#    data = request.get_json()
#    if "Username" in data:
#        playerList.append(data["Username"])
#        return "created !"
#    else:
#        return "Bad request", 400