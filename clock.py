from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from twilio_api_script import sendText

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(sendText, 'interval', hours=1)

sched.start()