from lunchstory import lunchstory
import schedule
import time 

schedule.every().day.at("00:00").do(lunchstory) 

while True: 
    schedule.run_pending() 
    time.sleep(1) 

