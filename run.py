#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
run bot
"""
import logging
import os
import telegram
from telegram.ext import Updater, CommandHandler, InlineQueryHandler
from telegram import InlineQueryResultVideo, InputTextMessageContent, InputTextMessageContent
from search import search_video, download
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

TOKEN = ''


def start(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="I'm a bot, please talk to me!")


def search(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    ret = search_video(query)
    if not ret:
        return
    for video in ret[:9]:
        results.append(
            InlineQueryResultVideo(
                video_url=video['arcurl'],
                mime_type="text/html",
                id=video['id'],
                thumb_url="http:"+video['pic'],
                title=clear_title(video['title']),
                parse_mode=telegram.ParseMode.HTML,
                input_message_content=InputTextMessageContent(video['arcurl']),
            )
        )
    bot.answer_inline_query(update.inline_query.id, results)


def clear_title(title):
    start_tag = "<em class=\"keyword\">"
    stop_tag = "</em>"
    return title.replace(start_tag, "").replace(stop_tag, "")


def main():
    updater = Updater(TOKEN=token)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    search_handler = InlineQueryHandler(search)
    dispatcher.add_handler(search_handler)
    dispatcher.add_handler(start_handler)

    PORT = int(os.environ.get('PORT', '8443'))
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN)
    updater.bot.set_webhook(
        "https://mighty-lowlands-79413.herokuapp.com/" + TOKEN)

    # updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
