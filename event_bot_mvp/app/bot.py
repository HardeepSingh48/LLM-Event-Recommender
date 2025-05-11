from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from app.db import Session, User
from app.llm_agent import extract_preferences

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! Tell me what kind of events you like and your city.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    msg = update.message.text
    parsed = extract_preferences(msg)

    # mock extraction
    prefs, city = "music, art", "Bangalore"

    session = Session()
    user = session.query(User).filter_by(telegram_id=user_id).first()
    if not user:
        user = User(telegram_id=user_id, preferences=prefs, city=city)
        session.add(user)
    else:
        user.preferences = prefs
        user.city = city
    session.commit()

    await update.message.reply_text(f"Got it! Will notify you when matching events happen in {city}.")

def run_bot():
    from os import getenv
    token = getenv("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
