from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from twilio_api_script import sendText
# count=0

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(sendText, 'interval', hours=8)

sched.start()