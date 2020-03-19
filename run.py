from flask import Flask


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from ca_app import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)
