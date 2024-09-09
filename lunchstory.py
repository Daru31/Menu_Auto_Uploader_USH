from selenium import webdriver # pip install selenium 
from PIL import Image # pip install pillow 
from pytesseract import * # pip install pytesseract 
import os 
from instagrapi import Client # pip install instagrapi 
import datetime 
# USERNAME, PASSWORD : 인스타 사용자명, 비밀번호 
# current_directory : 레포지토리 경로 

class lunchstory: 
    
    def web_capture(self): 
        driver = webdriver.Chrome() 
        driver.get("https://school.use.go.kr/ulsan-hs-h/M01030702") 

        for i in range(0, 1300, 100): 
            driver.execute_script(f"window.scrollTo(0, {i})") 
            if(i == 1200): 
                png = driver.get_screenshot_as_png() 
                open('lunch_screen'+str(i)+'.png', 'wb').write(png) 

        im = Image.open("current_directory/lunch_screen1200.png") 
        left = 250 # 감소 = 왼쪽으로 확장 
        right = 380 # 증가 = 오른쪽으로 확장 
        top = 70 # 감소 = 위로 확장 
        bottom = 480 # 증가 = 아래로 확장 

        im1 = im.crop((left, top, left + right, top + bottom)) 
        imgpath = "current_directory/crop_screen.png"  
        im1.save(imgpath)  
        
    def no_capture(self): 
        im = Image.open("current_directory/lunch_screen1200.png") 
        left = 250 # 감소 = 왼쪽으로 확장 
        right = 300 # 증가 = 오른쪽으로 확장 
        top = 260 # 감소 = 위로 확장 
        bottom = 150 # 증가 = 아래로 확장 
        
        im1 = im.crop((left, top, left + right, top + bottom)) 
        imgpath = "current_directory/crop_exception.png" 
        im1.save(imgpath) 
        
        image = Image.open(imgpath) # sample.txt 생성 
        text = image_to_string(image, lang="kor") 

        with open("sample.txt", "w", encoding="utf8") as img: 
            img.write(text) 
            
    def except_as_date(self): 
        file_path = 'sample.txt' 
        def contains_str(file_path): 
            with open(file_path, 'r', encoding='utf8') as file: 
                content = file.read() 
                return '알레르기 정보' in content 

        if os.path.exists(file_path): 
            if os.path.getsize(file_path) == 0: 
                print("No meal today. ") 
                quit() 
                
            elif contains_str(file_path): 
                print("only lunch today. ")
                im = Image.open("current_directory/lunch_screen1200.png") 
                left = 250 # 감소 = 왼쪽으로 확장
                right = 380 # 증가 = 오른쪽으로 확장
                top = 70 # 감소 = 위로 확장
                bottom = 250 # 증가 = 아래로 확장

                im1 = im.crop((left, top, left + right, top + bottom)) 
                imgpath = "current_directory/crop_screen.png" 
                im1.save(imgpath) 
                
            else: 
                print("lunch & dinner ") 
        
    def login_upload(self): 
        cl = Client()
        cl.delay_range = [1,3]
        cl.load_settings("session.json") 
        cl.delay_range = [1,3]
        cl.login('USERNAME', 'PASSWORD')  
        cl.delay_range = [1,3]
        cl.get_timeline_feed() 
        cl.delay_range = [1,3]

        cl.photo_upload_to_story('current_directory/crop_screen.png') 
        cl.delay_range = [1,3] 
    
    def timecheck(self): 
        print("Task completed at:", datetime.datetime.now()) 
        
        
run = lunchstory() 
run.web_capture() 
run.no_capture() 
run.except_as_date() 
run.login_upload() 
run.timecheck()
