from apscheduler.schedulers.blocking import BlockingScheduler
import pytz

from vol_sender import send_vol_data

send_time = (16,15)

def main():
    send_vol_data()
    print(f"Will send tomorrow's data at {send_time[0]}:{send_time[1]}.")
    

timez = pytz.timezone('Asia/Shanghai')

scheduler = BlockingScheduler(timezone=timez)
scheduler.add_job(main, 'cron', hour=send_time[0], minute=send_time[1])

try:
    print(f"Volatility data sender process initiated. The data will be sent today at {send_time[0]}:{send_time[1]}.")
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    pass