# utils/scheduler.py
import schedule
import time
from main import main

def run_bot():
    main()

# Schedule the bot to run daily at noon
schedule.every().day.at("12:00").do(run_bot)

while True:
    schedule.run_pending()
    time.sleep(60)
