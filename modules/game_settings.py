from modules.db_model import User
from modules.db_connection import db_session, db_commit


class SetDifficulty:
    def __init__(self, user_id):
        self.user = db_session.query(User).get(user_id)

    async def set_easy(self):
        self.user.difficulty = 0
        db_commit()

    async def set_medium(self):
        self.user.difficulty = 1
        db_commit()

    async def set_hard(self):
        self.user.difficulty = 2
        db_commit()


class SetOperations:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.user = db_session.query(User).get(user_id)

    @staticmethod
    def check_valid(user):
        return any([user.sub, user.sum, user.mul])

    def set_sum(self) -> str:
        self.user.sum = not self.user.sum
        if self.check_valid(self.user):
            db_commit()
            return GetSettings(self.user_id).as_msg()
        else:
            self.user.sum = not self.user.sum
            return 'Вы должны оставить хотя бы одну операцию!'

    def set_sub(self) -> str:
        self.user.sub = not self.user.sub
        if self.check_valid(self.user):
            db_commit()
            return GetSettings(self.user_id).as_msg()
        else:
            self.user.sub = not self.user.sub
            return 'Вы должны оставить хотя бы одну операцию!'

    def set_mul(self) -> str:
        self.user.mul = not self.user.mul
        if self.check_valid(self.user):
            db_commit()
            return GetSettings(self.user_id).as_msg()
        else:
            self.user.mul = not self.user.mul
            return 'Вы должны оставить хотя бы одну операцию!'


class GetSettings:
    def __init__(self, user_id):
        self.user = db_session.query(User).get(user_id)

    def as_msg(self) -> str:
        diffs = ['Легкий', 'Средний', 'Высокий']
        ops = []
        if self.user.sum:
            ops.append('+')
        if self.user.sub:
            ops.append('-')
        if self.user.mul:
            ops.append('*')

        message = f'Текущие настройки \n' \
                  f'Уровень сложности: {diffs[self.user.difficulty]} \n' \
                  f'Доступные операции: {" ".join(ops)}'

        return message

    def as_dict(self) -> dict:
        ops = []
        if self.user.sum:
            ops.append('+')
        if self.user.sub:
            ops.append('-')
        if self.user.mul:
            ops.append('*')

        settings = {
            'difficulty': self.user.difficulty,
            'ops': ' '.join(ops)
        }
        return settings
