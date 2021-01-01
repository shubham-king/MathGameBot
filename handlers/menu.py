from aiogram import types
from modules import math_game, user
from modules.keyboards import Keyboard as kb
from bot import dp
from modules.states import States
import modules.game_settings as gs


@dp.message_handler(state='*', commands=['start'])
async def process_start_command(message: types.Message):
    user.create_user(message.from_user.id)
    await States.menu.set()
    await message.reply('Привет! Я бот для тренировки счета в уме. '
                        'Для того чтобы начать, нажми кнопку "Новая игра"',
                        reply_markup=kb.menu_kb())


@dp.message_handler(state=States.menu)
async def response(message: types.Message):
    if message.text == 'Новая игра':
        await States.playing.set()
        await message.answer('Начали!',
                             reply_markup=kb.end_game_kb()
                             )
        math_game.create_game_session(message.from_user.id)
        task = await math_game.give_task(message.from_user.id)
        await message.answer(task)

    if message.text == 'Настройки':
        await States.settings_page_1.set()
        await message.answer(gs.GetSettings(message.from_user.id).as_msg(),
                             reply_markup=kb.settings_kb_page1())

    if message.text == 'Статистика':
        score = user.get_score(message.from_user.id)
        await States.statistic.set()
        await message.answer('Ваш лучший результат {}.'.format(score),
                             reply_markup=kb.return_kb())


