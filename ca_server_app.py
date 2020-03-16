from flask import Flask

ca_server_app = Flask(__name__)


@ca_server_app.route('/')
def main_page():
    return 'Welcome to the main page test'
