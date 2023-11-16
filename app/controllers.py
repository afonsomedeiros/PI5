from bottle import view, Bottle, request, response, redirect
from CONST import COOKIES_SECRET


def create_dashboard_route(app: Bottle):
    @app.get("/dashboard")
    @view("dashboard")
    def dashboard_get():
        return {}