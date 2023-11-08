from flask import Flask
from api.controllers import test


def create_routes(app: Flask):
    app.add_url_rule("/test", methods=["GET"], view_func=test.test)