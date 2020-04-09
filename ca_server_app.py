from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
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

ca_public_key_file = open("keys/ca_pub_key.pem", "rb")
ca_public_key = x509.load_pem_x509_certificate(ca_public_key_file.read(), default_backend())

ca_private_key_file = open('keys/ca_priv_key.pem', 'rb')
ca_private_key = serialization.load_pem_private_key(ca_private_key_file.read(), "passphrase".encode("utf-8"),
                                                    default_backend())


@app.route('/info', methods=['GET'])
def ca_get_tasks():
    return jsonify({'App info': info})


@app.route('/csr', methods=['POST'])
def ca_sign_csr():
    csr_from_request = request.data
    csr = x509.load_pem_x509_csr(csr_from_request, default_backend())
    file_name = request.headers.get('Filename')
    signed_csr = sign_csr(csr, ca_public_key, ca_private_key, file_name)
    return signed_csr


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')