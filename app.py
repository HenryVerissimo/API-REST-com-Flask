from app import app, db
from flask import request, jsonify


from app.controllers.user_controller import UserController
from app.models.mongodb import log_info


@app.route("/users", methods=["POST"])
def create_user():

    log_info(__name__, "Requisição para inserir um novo usuário")
    user_info = request.get_json()
    response = UserController().create_user(user_info)
    
    if response["status"] == "success":
        return jsonify(response), 201
    
    return jsonify(response), 400

@app.route("/users", methods=["GET"])
def select_users():

    log_info(__name__, "Requisição para visualizar todos os usuários")
    response = UserController().select_all_users()
    
    if response["status"] == "success":
        return jsonify(response), 200
    
    return jsonify(response), 400

@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id: int):

    log_info(__name__, "Requisição para atualizar um usuário")
    user_info = request.get_json()
    response = UserController().update_user_by_id(id, user_info)
    
    if response["status"] == "success":
        return jsonify(response), 200
    
    return jsonify(response), 400

@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id: int):

    log_info(__name__, "Requisição para deletar um usuário")
    response = UserController().delete_user_by_id(id)
    
    if response["status"] == "success":
        return jsonify(response), 200
    
    return jsonify(response), 400

@app.route("/users/<int:id>", methods=["GET"])
def select_user(id):

    log_info(__name__, "Requisição para visualizar um usuário")
    response = UserController().select_user_by_id(id)

    if response["status"] == "success":
        return jsonify(response), 200
    
    return jsonify(response), 400

if __name__ == "__main__":

    app.run(debug=True)
