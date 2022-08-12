from flask import Flask
from flask import request
app = Flask(__name__) 


@app.route('/hello/', methods=['GET', 'POST'])
def hello():
    return "got POST request"
