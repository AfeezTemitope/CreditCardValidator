from flask import request, jsonify
import re

def luhn_check(card_number):
    digits = [int(d) for d in card_number[::-1]]
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    total = sum(digits)
    return total % 10 == 0

def validate_card(card_number):
    pattern = r"[-/.*?,@]"
    cleaned_card_number = re.sub(pattern, '', card_number)

    if not cleaned_card_number.isdigit():
        return 'Invalid card number: only digits are allowed'

    length = len(cleaned_card_number)

    if length in [13, 16]:
        if cleaned_card_number.startswith('4'):
            return 'Visa'

    if length == 16:
        if cleaned_card_number.startswith(('51', '52', '53', '54', '55')):
            return 'MasterCard'
        if cleaned_card_number.startswith('6011') or cleaned_card_number.startswith(
                ('644', '645', '646', '647', '648', '649', '65')):
            return 'Discover'

    if length == 15:
        if cleaned_card_number.startswith(('34', '37')):
            return 'American Express'

    if length == 16:
        if cleaned_card_number.startswith(('506099', '650002', '650003', '650004')):
            return 'Verve'

    if length in range(16, 20):
        if cleaned_card_number.startswith('62'):
            return 'UnionPay'

    return 'Unknown card type'

def validate():
    card_number = request.json['card_number']
    card_type = validate_card(card_number)
    cleaned_card_number = re.sub(r"[-/.*?,@]", '', card_number)
    
    if not luhn_check(cleaned_card_number):
        return jsonify({'card_type': card_type, 'valid': False, 'message': 'Invalid card number according to Luhn algorithm'})
    
    return jsonify({'card_type': card_type, 'valid': True})