
from telebot import TeleBot, types

bot = TeleBot(token='6248003057:AAHjxCWdMixZ1M4whuVRs8I4UQszqjTDX8g', parse_mode='html') 

DEFINITOINS = {
    'регресс': 'Проверить что новый функционал не сломал существующий',
    'новое слово': 'тут его определение',
}


@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id, 
        text='Привет дорогой пользователь! Я помогу тебе расшифровать сложные аббревиатуры и термины 🤓\nВведи интересующий термин, например, смоук.\n Если хочешь узнать, кто тут главный, пиши - Кто создатель?', 
    )


@bot.message_handler()
def message_handler(message: types.Message):
    if message.text == 'Кто создатель?'
  bot.send_message(
        chat_id=message.chat.id,
        text='github.com - https://github.com/ElizawetSilko \n email - elizavetasylko@gmail.com \n telegram - https://t.me/elizavetafuchs \n Vk - https://vk.com/sylko0',
    )

    definition = DEFINITOINS.get(
        message.text.lower(), 
    )
    
    if definition is None:
    
        bot.send_message(
            chat_id=message.chat.id,
            text='😋 А что это у нас тут такое?',
        )
        return
    

    bot.send_message(
        chat_id=message.chat.id,
        text=f'Определение:\n<code>{definition}</code>',
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=f'Жду следующий термин',
    )


def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()
