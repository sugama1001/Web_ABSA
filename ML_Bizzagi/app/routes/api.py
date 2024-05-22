from flask import Blueprint, request, jsonify

blueprint = Blueprint('ml_api', __name__, url_prefix='/ml')

@blueprint.route('/predict', methods=['POST'])
def ml_predict():
    data = request.get_json()

    response = {
        'message': 'Data received successfully',
        'data': data
    }
    return jsonify(response), 200

