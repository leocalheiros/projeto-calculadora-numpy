from flask import request, jsonify
from .server import app


@app.route("/", methods="POST")
def calculator_function():
    pass
