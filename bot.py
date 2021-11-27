from telebot import TeleBot
from handler import Handler
"""
Done! Congratulations on your new bot. You will find it at t.me/snv1980_test_bot. 
You can now add a description, about section and profile picture for your bot, 
see /help for a list of commands. By the way, when you've finished creating your cool bot,
 ping our Bot Support if you want a better username for it. Just make sure the bot is fully 
 operational before you do this.

Use this token to access the HTTP API:
2134178627:AAHi5s4BgjrW5AN-ulNVyFPz98rY01KfOBU
Keep your token secure and store it safely, it can be used by anyone to control your bot.
"""

bot = TeleBot('2134178627:AAHi5s4BgjrW5AN-ulNVyFPz98rY01KfOBU')
handler = Handler()


@bot.message_handler(content_types=['text'])
def answer(message):
    bot.send_message(
        message.chat.id,
        handler.get_response(message.chat.id, message.text)
    )


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
