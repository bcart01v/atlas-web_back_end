#!/usr/bin/env python3
""" Flask App """
from flask import Flask, jsonify, request, abort, make_response, redirect, url_for
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


@app.route('/sessions', methods=['POST'])
def login():
    """ Login user and create session """
    email = request.form.get('email')
    password = request.form.get('password')

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)

    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie('session_id', session_id)

    return response


@app.route('/sessions', methods=['DELETE'])
def logout():
    """ Logout user and delete session """
    session_id = request.cookies.get('session_id')
    user = Auth.get_user_from_session_id(session_id)

    if not user:
        abort(403)

    AUTH.destroy_session(user.id)
    return redirect(url_for('home'))



@app.route('/', methods=['GET'])
def home():
    """ Return a JSON payload. """
    return jsonify({"message": "Bienvenue"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
