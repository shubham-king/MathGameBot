from aiogram import types
from modules.keyboards import Keyboard as kb
from bot import dp
from modules.states import States
import modules.game_settings as gs


@dp.message_handler(state=States.settings_page_1, regexp='Назад')
async def exit_from_settings(message: types.Message):
    await States.menu.set()
    await message.answer('Меню',
                         reply_markup=kb.menu_kb())


@dp.message_handler(state=States.settings_page_1, regexp='Выбор математических операций')
async def show_ops_settings(message: types.Message):
    await States.settings_page_2.set()
    await message.answer('Какие математические операции будут использоваться во время игры?',
                         reply_markup=kb.settings_kb_page2())
    await message.answer(gs.GetSettings(message.from_user.id).as_msg())


@dp.message_handler(state=States.settings_page_1)
async def set_difficulty(message: types.Message):
    if message.text == 'Легкий N * N':
        await gs.SetDifficulty(message.from_user.id).set_easy()
        await message.answer(gs.GetSettings(message.from_user.id).as_msg())
    elif message.text == 'Средний NN * N':
        await gs.SetDifficulty(message.from_user.id).set_medium()
        await message.answer(gs.GetSettings(message.from_user.id).as_msg())
    elif message.text == 'Высокий NN * NN':
        await gs.SetDifficulty(message.from_user.id).set_hard()
        await message.answer(gs.GetSettings(message.from_user.id).as_msg())
    else:
        await message.answer('Выбери значение из меню.')


@dp.message_handler(state=States.settings_page_2, regexp='Назад')
async def return_to_difficult_settings(message: types.Message):
    await States.settings_page_1.set()
    await message.answer(gs.GetSettings(message.from_user.id).as_msg(),
                         reply_markup=kb.settings_kb_page1())


@dp.message_handler(state=States.settings_page_2)
async def set_operations(message: types.Message):
    if message.text == 'Добавить / Убрать (+)':
        await message.answer(gs.SetOperations(message.from_user.id).set_sum())
    elif message.text == 'Добавить / Убрать (-)':
        await message.answer(gs.SetOperations(message.from_user.id).set_sub())
    elif message.text == 'Добавить / Убрать (*)':
        await message.answer(gs.SetOperations(message.from_user.id).set_mul())
    else:
        await message.answer('Выбери значение из меню.')
