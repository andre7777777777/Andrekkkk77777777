from asyncio import set_event_loop, new_event_loop
from datetime import datetime
from telethon.sync import TelegramClient
from dateutil.relativedelta import relativedelta
import random


def cryptopizza_news(id):
    set_event_loop(new_event_loop())
    api_id = 24643088
    api_hash = '360c79a7cb1e41fddbd699db52ca3ddb'

    posts = []
    a = 0
    with TelegramClient('sv1pone', api_id, api_hash) as client:
        for message in client.iter_messages(id):
            date, time = str(message.date).split('+')[0].split(' ')
            years, months, days = date.split('-')
            hours = time.split(':')[0]
            diff = (datetime.now() - relativedelta(years=int(years) - 2, months=int(months), days=int(days),
                                                   hours=int(hours))).hour
            if diff == 0 and a:
                break
            else:
                posts.append(message.text)
            a = 1

    if len(posts) > 3:
        posts = random.sample(posts, 3)

    return posts
