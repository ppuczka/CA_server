from flask import Flask, make_response, jsonify, request

ca_server_app = Flask(__name__)


@ca_server_app.route('/')
def main_page():
    return 'Welcome to the main page test'


@ca_server_app.route('/api/ca/certificate', methods=['GET', 'POST'])
def rest_page():
    if request.method == 'GET':
        return 'Welcome'
    elif request.method == 'POST':
        csr = request.args.get('csr', '')
        print(f'This is where csr should be {csr}')
        return csr
#
#
# @ca_server_app.errorhandler('404')
# def not_found():
#     return make_response(jsonify({'error': 'Not found'}), 404)

