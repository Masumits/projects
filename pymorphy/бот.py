#бот, работающий только на моем компе
import telebot  # импортируем модуль pyTelegramBotAPI
import conf     # импортируем наш секретный токен
import genSent  # импортируем нашу программу, которая делает ответ

bot = telebot.TeleBot(conf.TOKEN)  # создаем экземпляр бота

bot.remove_webhook()#удаляем все вебхуки

# этот обработчик запускает функцию send_welcome, когда пользователь отправляет команды /start или /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Это бот, который генерирует согласованное предложение")
    
@bot.message_handler(func=lambda m: True)  # этот обработчик реагирует на любое сообщение
def send_len(message):
        resp = genSent.makeResponse(message.text)
        bot.send_message(message.chat.id, resp)


if __name__ == '__main__':
    bot.polling(none_stop=True)
