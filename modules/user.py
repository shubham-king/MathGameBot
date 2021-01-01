from modules.db_model import User
from modules.db_connection import db_session, db_commit


def create_user(user_id: int):
    new_user = User(id=user_id)
    db_session.add(new_user)
    db_commit()


def get_score(user_id: int):
    user = db_session.query(User).get(user_id)
    return user.score
