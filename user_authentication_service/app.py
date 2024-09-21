#!/usr/bin/env python3
""" Flask App """
from flask import Flask, jsonify, request
from auth import Auth


app = Flask(__name__)

AUTH = Auth()


@app.route('/users', methods=['POST'])
def users():
    """ endpoint to register a new user """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return jsonify({"message": "email and password is required"}), 400

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already exists"}), 400


@app.route('/', methods=['GET'])
def home():
    """ Return a JSON payload. """
    return jsonify({"message": "Bienvenue"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
