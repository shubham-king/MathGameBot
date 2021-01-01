import random
import redis
from modules.game_settings import GetSettings
from modules.db_connection import db_session, db_commit
from modules.db_model import User

redis_con = redis.Redis(host='redis', port=6379)


def create_game_session(user_id: int):
    settings = GetSettings(user_id).as_dict()
    game_session = {'true_answer': 0,
                    'right_answers': 0,
                    'false_answers': 0,
                    'difficulty': settings['difficulty'],
                    'operations': settings['ops']}

    redis_con.hmset(user_id, game_session)


async def give_task(user_id: int) -> str:
    difficulty = int(redis_con.hget(user_id, 'difficulty'))
    operations = redis_con.hget(user_id, 'operations').decode('utf-8').split()
    if difficulty == 0:
        n1 = random.randint(1, 9)
        n2 = random.randint(1, 9)
    elif difficulty == 1:
        n1 = random.randint(10, 99)
        n2 = random.randint(1, 9)
    elif difficulty == 2:
        n1 = random.randint(1, 99)
        n2 = random.randint(1, 99)
    operation = random.choice(operations)
    if operation == '-' and n2 > n1:
        n1, n2 = n2, n1
    answer = await solve_task(n1, n2, operation)
    redis_con.hset(user_id, 'true_answer', answer)
    task = '{} {} {} = ?'.format(n1, operation, n2)
    return task


async def solve_task(n1: int, n2: int, op: str) -> int:
    if op == '+':
        return int(n1) + int(n2)
    elif op == '-':
        return int(n1) - int(n2)
    elif op == '*':
        return int(n1) * int(n2)


async def check_task(user_id: int, answer: int) -> str:
    result = int(redis_con.hget(user_id, 'true_answer')) == int(answer)
    if result:
        redis_con.hincrby(user_id, 'right_answers', 1)
        result = 'Верно!'
    else:
        redis_con.hincrby(user_id, 'false_answers', 1)
        result = 'Неверно!'

    return result


async def get_results(user_id: int) -> str:
    sum_right_answers = int(redis_con.hget(user_id, 'right_answers'))
    sum_false_answers = int(redis_con.hget(user_id, 'false_answers'))
    count = sum_right_answers + sum_false_answers
    msg = f'Решено примеров: {count} \n'\
          f'Правильных ответов: {sum_right_answers} \n'\
          f'Неправильных ответов: {sum_false_answers}'

    return msg


async def set_new_highscore(user_id: int):
    user = db_session.query(User).get(user_id)
    cur_score = user.score
    new_score = int(redis_con.hget(user_id, 'right_answers'))
    if new_score > cur_score:
        user.score = new_score
        db_commit()
