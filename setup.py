# repeat.py 실행 전 먼저 실행해야하는 코드 

from instagrapi import Client 

cl = Client()
cl.login('USERNAME', 'PASSWORD')
cl.dump_settings("session.json") 


