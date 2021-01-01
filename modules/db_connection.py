from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from modules.db_model import Base
import logging

engine = create_engine('sqlite:///math_game.db')
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

db_session = Session()


def db_commit():
    try:
        db_session.commit()
    except Exception as e:
        db_session.rollback()
        logging.error(
            'Error is {}'.format(e))


if not os.path.isfile('../math_game.db'):
    Base.metadata.create_all(engine)
