import json
from datetime import datetime
from telegram import Bot
from app.db import Session, User

def check_events():
    with open("app/events.json") as f:
        events = json.load(f)

    session = Session()
    users = session.query(User).all()
    from os import getenv
    token = getenv("TELEGRAM_TOKEN")
    bot = Bot(token=token)

    for user in users:
        for event in events:
            if event["city"].lower() == user.city.lower() and event["category"] in user.preferences:
                event_date = datetime.strptime(event["date"], "%Y-%m-%d")
                if (event_date - datetime.now()).days <= 3:
                    bot.send_message(chat_id=user.telegram_id,
                                     text=f"🎉 Upcoming event: {event['title']} in {event['city']} on {event['date']}")
