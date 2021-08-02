from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request

scheduleEvent = BlockingScheduler()

@scheduleEvent.scheduled_job('cron',day_of_week='mon-fri',minute='*/20')
def scheduled_job():
    website = "https://mylinebothellotux.herokuapp.com/"
    connection = urllib.request.urlopen(website)

    for i, value in connection.getheaders():
        print(i,value)

scheduleEvent.start()