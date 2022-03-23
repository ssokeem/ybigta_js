from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import urllib.request  # 이미지 저장 모듈

service = Service(executable_path=ChromeDriverManager().install())

# 사용자 정의 검색어 받아오기 - Type your answer
keyword = '강아지'

# 폴더 만들기
if not os.path.exists(f'{keyword}'):   # 해당 폴더의 존재여부를 boolean값으로 출력해줌
    # not True = False : 해당폴더가 기존에 존재하지 않으면 새 폴더를 만든다!
    os.mkdir(f'{keyword}')  

url = f'https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query={keyword}'
browser = webdriver.Chrome(service=service)
browser.implicitly_wait(5) 
browser.maximize_window() # 화면크기 최대화
browser.get(url)  
time.sleep(2)

# 무한스크롤 - Type your answer

before_h = browser.execute_script("return window.scrollY")

while True:
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
    time.sleep(1)
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:
        break
    before_h = after_h

# 이미지 태그 추출
imgs = browser.find_elements(By.CSS_SELECTOR, 'img._image._listImage')

for i, img in enumerate(imgs, 1):   # enumerate(대상, 시작값)
    # 이미지 다운을 위해선 태그에있는 이미지의 주소가 필요하다.
		# Type your answer
    img_src = img.get_attribute('src')
    print(i, img_src)
    # img를 index값의 파일명으로 png파일로 저장
    urllib.request.urlretrieve(img_src, f'{keyword}/{i}.png')