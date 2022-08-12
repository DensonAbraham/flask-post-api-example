from flask import Flask
from flask import request
from flask_cors import CORS
app = Flask(__name__) 

CORS(app)
@app.route('/hello/', methods=['GET', 'POST'])
def hello():
    return "got POST request"
