from flask import Blueprint, jsonify, Response, request, current_app


def test():
    Response.content_type = 'Application/json'
    return jsonify({"teste": "Olá mundo"}), 200
