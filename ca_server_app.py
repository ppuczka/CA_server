import os

from flask import Flask, jsonify, request

from ca_helpers import sign_csr

app = Flask(__name__)

info = [
    {
        'title': u'CA Server App',
        'description': 'Sign Your Certificate Signing Request',
    },
    {
        'endpoint': '/csr',
        'action': 'POST',
        'description': 'Post Your CSR here to receive signed key'
    }
]

pk_file = open('/Users/ppuczka/Desktop/Projects_v2/py_cli/ca_priv_key.pem', 'r')
pub_file = open('/Users/ppuczka/Desktop/Projects_v2/py_cli/ca_pub_key.pem', 'r')


@app.route('/info', methods=['GET'])
def get_tasks():
    return jsonify({'App info': info})


@app.route('/csr', methods=['POST'])
def read_csr():
    private_key = pk_file.read()
    pk_file.close()
    public_key = pub_file.read()
    pub_file.close()
    csr = request.data
    file_name = request.headers.get('Filename')
    signed_csr = sign_csr(csr, public_key, private_key, file_name)
    print(signed_csr)
    return signed_csr


if __name__ == '__main__':
    app.run(debug=True)