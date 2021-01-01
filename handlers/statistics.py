from aiogram import types
from modules.keyboards import Keyboard as kb
from bot import dp
from modules.states import States


@dp.message_handler(state=States.statistic, regexp='Назад')
async def exit_from_stat(message: types.Message):
    await States.menu.set()
    await message.answer('Меню', reply_markup=kb.menu_kb())