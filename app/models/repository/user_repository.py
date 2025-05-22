from app.models.entities import db, User

class UserRepository:
    def insert(self, name: str, email: str, password: str) -> User | None:
        new_user = User(name, email, password)

        with db.session() as session:
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
        
        return new_user
    
    def select_all(self) -> list:
        with db.session() as session:
            users = session.query(User).all()
            for user in users:
                session.refresh(user)
        
        return users
        
    
    def select_quant(self, quantity: int) -> list:
        with db.session() as session:
            users = session.query(User).count(quantity)
            session.refresh(users)

        return users

    def select_by_email(self, email: str) -> User | None:
        with db.session() as session:
            user = session.query(User).filter_by(email=email).first()
            if user: 
                session.refresh(user)

        return user
    
    def select_by_id(self, id: int) -> User | None:
        with db.session() as session:
            user = session.query(User).filter_by(id=id).first()
            if user:
                session.refresh(user)

        return user
    
    def update_by_id(self, id: int, name: str, email: str, password: str) -> User:
        with db.session() as session:
            user = session.query(User).filter_by(id=id).first()

            if user:
                user.name = name
                user.email = email
                user.password = password

                session.add(user)
                session.commit()
                session.refresh(user)

        return user