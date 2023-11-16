from bottle import Bottle
from .controllers import create_dashboard_route


def create_app():
    app = Bottle()
    create_dashboard_route(app)
    return app