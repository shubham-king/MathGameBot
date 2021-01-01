from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


class Keyboard:
    @staticmethod
    def menu_kb() -> ReplyKeyboardMarkup:
        start_button = KeyboardButton('Новая игра')
        settings_button = KeyboardButton('Настройки')
        statistic_button = KeyboardButton('Статистика')
        kb = ReplyKeyboardMarkup(resize_keyboard=True).add(start_button).add(statistic_button).add(settings_button)
        return kb

    @staticmethod
    def end_game_kb() -> ReplyKeyboardMarkup:
        back_button = KeyboardButton('Закончить игру')
        kb = ReplyKeyboardMarkup(resize_keyboard=True).add(back_button)
        return kb

    @staticmethod
    def settings_kb_page1() -> ReplyKeyboardMarkup:
        set_easy = KeyboardButton('Легкий N * N')
        set_medium = KeyboardButton('Средний NN * N')
        set_hard = KeyboardButton('Высокий NN * NN')
        set_ops = KeyboardButton('Выбор математических операций')
        back = KeyboardButton('Назад')
        kb = ReplyKeyboardMarkup(resize_keyboard=True)
        kb.add(set_easy).add(set_medium).add(set_hard).add(set_ops).add(back)
        return kb

    @staticmethod
    def settings_kb_page2() -> ReplyKeyboardMarkup:
        set_sum = KeyboardButton('Добавить / Убрать (+)')
        set_sub = KeyboardButton('Добавить / Убрать (-)')
        set_mul = KeyboardButton('Добавить / Убрать (*)')
        back = KeyboardButton('Назад')
        kb = ReplyKeyboardMarkup(resize_keyboard=True)
        kb.add(set_sum).add(set_sub).add(set_mul).add(back)
        return kb

    @staticmethod
    def return_kb() -> ReplyKeyboardMarkup:
        back_button = KeyboardButton('Назад')
        kb = ReplyKeyboardMarkup(resize_keyboard=True).add(back_button)
        return kb
