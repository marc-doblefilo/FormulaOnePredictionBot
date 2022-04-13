# coding=utf-8
from application import bot
from model.league import League
from model.user import User
from shared.tables import create_standings_table


@bot.message_handler(commands=['standings'])
def register(message):

    chatId = message.chat.id

    if chatId > 0:
        bot.reply_to(
            message, "This is not a group. Please use this command in a group 😔", parse_mode='Markdown')
        return

    if League.get(chatId) == None:
        bot.reply_to(
            message, "There is no league in this group yet. Use the command /startleague to start it! 😎", parse_mode='Markdown')
        return

    users = User.get_all_from_a_league(chatId)
    ordered_users = sorted(users, key=lambda x: x.points, reverse=True)
    table = create_standings_table(ordered_users)

    bot.reply_to(message, f'<pre>{table}</pre>',
                 parse_mode='HTML')
