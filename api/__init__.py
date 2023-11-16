from bottle import Bottle
from api.extension import install_jwt_bottle
from api.controller import create_controllers


def create_app():
    app = Bottle()

    install_jwt_bottle(app)
    create_controllers(app)

    return app