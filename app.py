from flask import Flask
from flask_cors import CORS

from urls import validate_card_input

app = Flask(__name__)
CORS(app)
# CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})
app.register_blueprint(validate_card_input)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
