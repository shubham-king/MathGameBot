from aiogram.dispatcher.filters.state import StatesGroup, State


class States(StatesGroup):
    menu: State = State()
    playing: State = State()
    settings_page_1: State = State()
    settings_page_2: State = State()
    statistic: State = State()