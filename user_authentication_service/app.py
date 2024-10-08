#!/usr/bin/env python3
""" Flask App """
from flask import Flask, jsonify, request, abort, make_response
from flask import Flask, redirect, url_for
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
    user = AUTH.get_user_from_session_id(session_id)

    if not user:
        abort(403)

    AUTH.destroy_session(user.id)
    return redirect(url_for('home'))


@app.route('/profile', methods=['GET'])
def profile():
    """ Get user profile """

    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if not user:
        abort(403)

    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    email = request.form.get('email')

    try:
        reset_token = AUTH.get_reset_password_token(email)
    except ValueError:
        return jsonify({"message": "email not found"}), 403

    return jsonify({"email": email, "reset_token": reset_token}), 200


@app.route('/reset_password', methods=['PUT'])
def update_password():
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')

    if not email or not reset_token or not new_password:
        return jsonify({"message": "Missing required inputs"}), 400

    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        return jsonify({"message": "Invalid reset token"}), 403

    return jsonify({"email": email, "message": "Password updated"}), 200


@app.route('/', methods=['GET'])
def home():
    """ Return a JSON payload. """
    return jsonify({"message": "Bienvenue"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
