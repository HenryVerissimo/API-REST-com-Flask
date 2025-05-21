from app import app, db
from flask import request, jsonify

from app.controllers.user_controller import UserController

@app.route("/users", methods=["POST"])
def create_user():
    user_info = request.get_json()
    response = UserController().create_user(user_info)

    if response["status"] == "success":
        return jsonify(response), 201
    
    return jsonify(response), 400

@app.route("/users", methods=["GET"])
def select_users():
    response = UserController().select_all_users()

    if response["status"] == "success":
        return jsonify(response), 200
    
    return jsonify(response), 400


if __name__ == "__main__":

    app.run(debug=True)
