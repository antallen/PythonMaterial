from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request
from app.dataSQL import connectDB
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from app import line_bot_api, handler

scheduleEvent = BlockingScheduler()
#@scheduleEvent.scheduled_job('interval',minutes=1)
#def timed_job():
#    msg = connectDB.showAds()
#    print(msg)
#    line_bot_api.push_message("你的ID",TextSendMessage(text=str(msg)))

@scheduleEvent.scheduled_job('cron',day_of_week='mon-fri',minute='*/20')
def scheduled_job():
    website = "https://mylinebothellotux.herokuapp.com/"
    connection = urllib.request.urlopen(website)

    for i, value in connection.getheaders():
        print(i,value)

scheduleEvent.start()