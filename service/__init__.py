from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from flask_talisman import Talisman


def create_app():
    app = Flask(__name__)

    CORS(app)

    Talisman(
        app,
        content_security_policy=None,
        force_https=False
    )

    api = Api(
        app,
        version="1.0",
        title="Accounts Service",
        description="Customer Accounts Microservice"
    )

    from .routes import api as accounts_ns
    api.add_namespace(accounts_ns)

    return app


app = create_app()
