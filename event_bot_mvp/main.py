from apscheduler.schedulers.background import BackgroundScheduler
from app.bot import run_bot
from app.event_checker import check_events

scheduler = BackgroundScheduler()
scheduler.add_job(check_events, 'interval', hours=6)
scheduler.start()
print("Scheduler started. Running event checker every 6 hours.")

print("Starting bot...")
run_bot()
