# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from bardapi import core as bard

# app = Flask(__name__)
# CORS(app)

# app.config['JSON_SORT_KEYS'] = False

# token = 'WQgjUQ5kvoFes5Vls82gwQPLeZ2p2hpQpv6x3TL2fPVVKRlXNoguWijrTnlfeTcWduQjlQ.'

# @app.route('/get_answer', methods=['POST'])
# def get_answer():
#     message = request.json.get('message')
#     response = bard.Bard(token).get_answer(message)
#     return jsonify(response)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
from bardapi import core as bard

app = Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS'] = False

token = 'ZQgjUcISkqAXa_bUUzzdL1t9JXGGWqDI2c2g5YI84Yf6AAAWijATjJLGhXlzwR0ld4hp4g.'

@app.route('/get_answer', methods=['POST'])
def get_answer():
    message = request.json.get('message')
    response = bard.Bard(token).get_answer(message)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)




