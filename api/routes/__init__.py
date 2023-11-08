from flask import Flask

from . import test

def create_routes(app: Flask):
    test.create_routes(app)