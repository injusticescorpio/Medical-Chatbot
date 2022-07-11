
from apscheduler.schedulers.background import BackgroundScheduler

# Creates a default Background Scheduler
sched = BackgroundScheduler()
def prompt(task):
    print(f"Executing Task...{task}")

def add_jump(time):
    sched.add_job(prompt, 'interval', seconds=time,args=[time])

add_jump(2)

