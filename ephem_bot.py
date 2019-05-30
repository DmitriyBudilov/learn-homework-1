"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime as dt
from config import PROXY, TOKEN
import logging
import ephem

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def list_of_planets_maker():
    '''
        Формирование списка планет.
        Из списка убраны Луна и Солнце
    '''
    planets = []
    for val in ephem._libastro.builtin_planets():
        if val[1] == 'Planet':
            planets.append(val[2])
    return planets[:-2]

def greet_user(bot, update):
    text = 'Called /start'
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    '''
        Функция возвращает текст переданный пользователем.
    '''
    user_text = 'Hi {}, you write {}!'.format(update.message.chat.first_name, update.message.text)
    logging.info('User: %s, Chat_id: %s, Message: %s', update.message.chat.username,
                                                    update.message.chat.id,
                                                    update.message.text)
    update.message.reply_text(user_text)

def give_me_planet(bot, update):
    '''
        Функция получает имя планеты от пользователя и возвращает имя созвездия в котором оно находится.
    '''
    list_of_planets = list_of_planets_maker()
    planet = update.message.text
    planet = planet.split()[1]
    
    if planet in list_of_planets: # Если планета в списке планет - передаём её ephem.
        planet_now = getattr(ephem, planet)(dt.now())
        constellation = ephem.constellation(planet_now)
        # Формируем строку ответа.
        response = '{planet} is now in the constellation {constellation}.'.format(planet=planet, constellation=constellation[1])
        update.message.reply_text(response)
    else: # Если планеты нет в списке планет - это не планета.
        # Формируем строку ответа.
        response = '{} is not a planet.'.format(planet)
        update.message.reply_text(response)

def main():
    mybot = Updater(TOKEN, request_kwargs=PROXY)

    logging.info('Bot starts.')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', give_me_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
