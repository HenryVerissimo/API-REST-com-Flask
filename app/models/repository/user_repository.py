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
            session.commit()
            for user in users:
                session.refresh(user)
        
        return users
        
    
    def select_quant(self, quantity: int) -> list:
        with db.session() as session:
            users = session.query(User).count(quantity)
            session.commit()
            session.refresh(users)

        return users

    def select_by_email(self, email: str) -> User | None:

        with db.session() as session:
            user = session.query(User).filter_by(email=email).first()
            if user: 
                session.refresh(user)

        return user