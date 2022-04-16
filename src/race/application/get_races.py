# coding=utf-8
from application import bot
from src.race.domain.race import Race
from src.race.infrastructure.get_current_races import get_current_races


@bot.message_handler(commands=['races'])
def get_races(message):
    chatId = message.chat.id
    username = message.from_user.username

    if(username != 'marc_doblefilo'):
        return

    total = Race.set()
    bot.reply_to(message, f'A total of {total} new races were saved.',
            parse_mode='Markdown')
