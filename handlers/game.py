from aiogram import types
from modules import math_game
from bot import dp
from modules.keyboards import Keyboard as kb
from modules.states import States


@dp.message_handler(state=States.playing, regexp='Закончить игру')
async def return_to_menu(message: types.Message):
    await States.menu.set()
    msg = await math_game.get_results(message.from_user.id)
    await math_game.set_new_highscore(message.from_user.id)
    await message.answer(
        msg,
        reply_markup=kb.menu_kb()
    )


@dp.message_handler(state=States.playing)
async def check_task(message: types.Message):
    try:
        int(message.text)
    except ValueError:
        await message.reply('Введи число или нажми "Закончить игру"')
        return
    result = await math_game.check_task(message.from_user.id, message.text)
    await message.reply(str(result))
    task = await math_game.give_task(message.from_user.id)
    await message.answer(task)
