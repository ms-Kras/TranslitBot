import os
import logging
from string import punctuation
from aiogram import Bot,Dispatcher,executor,types
logging.basicConfig(level=logging.INFO)
TOKEN = os.getenv('TOKEN')

tranlit = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
         'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
         'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'y', 'ъ': 'ie', 'э': 'e',
         'ю': 'iu', 'я': 'ia'}

bot=Bot(token=TOKEN)
dp=Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def send_welcome(message:types.Message):
    user_name=message.from_user.full_name
    user_id=message.from_user.id
    greetings=f'Привет, {user_name}! Введи свои ФИО кириллицей'
    logging.info(f'{user_name=} {user_id=} sent message: {message.text}')
    await bot.send_message(user_id, greetings)

@dp.message_handler()
async def send_welcome(message:types.Message):
    user_name=message.from_user.full_name
    user_id=message.from_user.id
    text=message.text
    text = text.lower()
    transtext = ''.join(tranlit.get(x, x) if x not in punctuation and x != 'ь' else x for x in text)
    transtext = ' '.join(x.capitalize() for x in transtext.split())
    transtext = transtext.replace('ь', '')
    logging.info(f'{user_name=} {user_id=} sent message: {message.text}')
    await bot.send_message(user_id, transtext)

if __name__ == '__main__':
    executor.start_polling(dp)