# coding=utf-8
from application import bot
from src.league.domain.league import League
from src.user.domain.user import User
from src.shared.tables import create_standings_table


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

    users = User.get_all_from_a_league_order_by_points(chatId)
    table = create_standings_table(users)

    bot.send_message(chatId, f'<b>{League.get(chatId).leagueName}</b>\n<pre>{table}</pre>',
                parse_mode='HTML')
