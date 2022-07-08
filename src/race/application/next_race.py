# coding=utf-8
import logging
import pytz

from application import bot
from src.race.infrastructure.get_next_race_schedule import get_next_race_schedule
from utils.extract_arguments import extract_arguments_without_command


@bot.message_handler(commands=['nextrace'])
def next_race(message):
    chatId = message.chat.id

    if chatId > 0:
        bot.reply_to(
            message, "This is not a group. Please use me only in groups 😔", parse_mode='Markdown')
        return

    arguments = extract_arguments_without_command(message.text)

    if len(arguments) > 1:
        bot.reply_to(
            message, "Sorry, make sure you use the timezone correctly Continent/Capital_City. For example: /nextrace Europe/Madrid", parse_mode='HTML')
        return

    if len(arguments) == 1 and arguments[0] not in pytz.all_timezones:
        bot.reply_to(
            message, "Sorry, make sure you use the timezone correctly Continent/Capital_City. For example: /nextrace Europe/Madrid", parse_mode='HTML')
        return

    message_text: str = ''

    schedule = get_next_race_schedule()
    ordered_sessions = sorted(schedule, key=schedule.get)
    if len(arguments) == 1 and arguments[0] != None:
        timezone = pytz.timezone(arguments[0])
        for session in ordered_sessions:
            date = schedule[session]
            converted_date = date.astimezone(timezone)
            message_text += f'*{session}:* {converted_date.strftime("%A at %H:%M; %d %B %Z")}\n'
    else:
        for session in ordered_sessions:
            message_text += f'*{session}:* {schedule[session].strftime("%A at %H:%M; %d %B %Z")}\n'

    bot.reply_to(message, f'{message_text}', parse_mode='Markdown')
