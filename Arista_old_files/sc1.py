from apscheduler.schedulers.background import BackgroundScheduler

# Creates a default Background Scheduler
sched = BackgroundScheduler()
i=0
sched.start()
def prompt(text):
    print("Executing Task...",text)

while True:
    if i==5:
        sched.add_job(prompt, 'interval', seconds=1,args=['i==5'])
    if i==7:
        sched.add_job(prompt, 'interval', seconds=2, args=['i==7'])
    i+=1

