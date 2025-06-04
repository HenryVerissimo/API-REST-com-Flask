from app.models.mysql.repository.user_repository import UserRepository
from app.models.mysql.entities.entities import user_schema, users_schema

from flask import jsonify

class UserController:

    def create_user(self, user_info: dict) -> dict:
        name = user_info["name"]
        email = user_info["email"]
        password = user_info["password"]

        if self.__verify_connection_db():
            return {"status": "error", "message": "Erro de conexão com o banco de dados!", "response": None}

        if self.__verify_email(email):
            return {"status": "error", "message": "Esse email já está sendo utilizado!", "response": None}

        try:
            repository = UserRepository()
            User = repository.insert(name, email, password)
            user_info = user_schema.dump(User)
            return {"status": "success", "message": "Registro cadastrado com sucesso!", "response": user_info}       

        except Exception as error:
            return {"status": "error", "message": "Erro ao tentar cadastrar registro", "response": str(error)}
        
    def select_all_users(self) -> list:
        try:
            repository = UserRepository()
            users = repository.select_all()
        
            if users:
                users_info =users_schema.dump(users)
                return {"status": "success", "message": "Registros encontrados com sucesso!", "response": users_info}
            
            return {"status": "success", "message": "Nenhum registro encontrado", "response": None}
        
        except Exception as error:
            return {"status": "error", "message": "Erro ao tentar encontrar registros", "response": str(error)} 

    def select_user_by_email(self, email: str) -> dict:
        try:
            repository = UserRepository()
            user = repository.select_by_email(email)

            if user:
                user_info = user_schema.dump(user)
                return {"status": "success", "message": "Registro encontrado com sucesso!", "response": user_info}
            
            return {"status": "success", "message": "Nenhum registro encontrado", "response": None}

        except Exception as error:
            return {"status": "error", "message": "Erro ao tentar procurar pelo registro", "response": str(error) }
        
    def select_user_by_id(self, id: int) -> dict:
        try:
            repository = UserRepository()
            user = repository.select_by_id(id)

            if user:
                user_info = user_schema.dump(user)
                return {"status": "success", "message": "registro encontrado com sucesso", "response": user_info}
            
            return {"status": "succes", "message": "Nenhum registro foi encontrado", "response": None}
        
        except Exception as error:
            return {"status": "error", "message": "Erro ao tentar procurar pelo registro", "respone": error}
        
    def update_user_by_id(self, id: int, user_info: dict) -> dict:
        id = int(id)
        name = user_info["name"]
        email = user_info["email"]
        password = user_info["password"]

        try:
            repository = UserRepository()
            user = repository.update_by_id(id, name, email, password)

            if user:
                user_info = user_schema.dump(user)
                return {"status": "success", "message": "Registro atualizado com sucesso!", "response": user_info}
            
            return {"status": "success", "message": "Nenhum registro encontrado", "response": None}
        
        except Exception as error:
            return {"status": "error", "message": "Erro ao tentar procurar pelo registro", "response": str(error) }
        
    def delete_user_by_id(self, id: int) -> dict:
        try:
            repository = UserRepository()
            response = repository.delete_by_id(id)

            if response:
                return {"status": "success", "message": "Registro deletado com sucesso"}
            
            return {"status": "success", "message": "Nenhum registro com esse ID foi encontrado"}
        
        except Exception as error:
            return {"status": "error", "message": "Erro ao tentar excluir registro!", "response": error}


    def __verify_email(self, email: str) -> bool:
        response = self.select_user_by_email(email)
        return response["status"] == "success" and response["response"] != None
    
    def __verify_connection_db(self) -> bool:
        response = self.select_all_users()
        return response["status"] == "error"


