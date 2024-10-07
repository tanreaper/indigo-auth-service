from flask import Flask
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
CORS(app)


@app.route("/")
@cross_origin()
def index ():
    return "<p>Welcome to Flask API</p>"

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT', 8081))
    app.run(host='0.0.0.0', port=port)