from time import sleep
from apscheduler.schedulers.background import BlockingScheduler

# Creates a default Background Scheduler
sched = BlockingScheduler()


def prompt():
    print("Executing Task...")


sched.add_job(prompt, 'interval', seconds=5)

sched.start()