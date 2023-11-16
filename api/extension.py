from bottle import Bottle
from jwt_bottle import JWTPlugin

from data.Auth import Auth


configs = [
    {'model': Auth, 'endpoint': '/auth', 'auth_name': "auth", 'refresh_name': 'refresh'}
]


def install_jwt_bottle(app: Bottle):
    jwt = JWTPlugin("abcde", configs=configs, payload=['_id', 'code', 'email', 'name'])

    app.install(jwt)