from flask import Blueprint
from views import validate
from flask_cors import CORS

validate_card_input = Blueprint('validate_card_input', __name__)
CORS(validate_card_input)


@validate_card_input.post('/validate')
def validate_card_route():
    return validate()
