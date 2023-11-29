import telebot

bot = telebot.TeleBot('6588346012:AAGWEzfG9ZaNsgJB7f6r3n6JDvnGsjEZir8')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Здравствуй, дорогой Друг! \nХочешь больше узнать о нашем продукте???',
                     parse_mode='Markdown')


@bot.message_handler(commands=['information'])
def run(message):
    bot.send_message(message.chat.id,
                     'Носки из на натуральной пряжи льна и крапивы позволяет ногам «дышать», создавая комфорт вашим ногам в жаркий и в холодный сезон. Не зря же раньше тяжелобольных  накрывали крапивным покрывалом, так  как  крапива улучшает кровообращение.[ссылка в магазин](https://vk.com/jul.nurik)',
                     parse_mode='Markdown')


bot.infinity_polling()