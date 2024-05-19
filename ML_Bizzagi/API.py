from flask import Flask, request, jsonify


app = Flask(__name__)

#post to for predict ABSA 
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    response = {
        'message': 'Data received successfully',
        'data': data
    }
    return jsonify(response), 200



