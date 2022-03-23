from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  # 크롬드라이버 자동업데이트
import time

service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

# 웹페이지 주소 이동
browser.get("https://www.naver.com")
time.sleep(2)

browser.find_element(By.CSS_SELECTOR, 'a.nav.shop').click()
time.sleep(1)

# 검색창 찾기 = 클릭
search = browser.find_element(By.CSS_SELECTOR, 'input.co_srh_input._input')

# 검색어 입력
search.send_keys('아이폰13')
search.send_keys(Keys.ENTER)

time.sleep(1)

# 스크롤 전 높이
before_h = browser.execute_script("return window.scrollY") #execute_script = 자바스크립트 명령어 실행

# 무한 스크롤 - 반복문
while True:
    # 맨 아래로 스크롤을 내린다. body = 모든 웹사이트에 존재
    # 키보드의 END키 누르면 웹페이지 맨아래로이동
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
    time.sleep(1) # 스크롤 사이 페이지 로딩시간
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:
        break
    before_h = after_h  # 스크롤 후 높이가 다르면 before_h를 업데이트
    
items = browser.find_elements(By.CSS_SELECTOR, 'li.basicList_item__2XT81')

i = 1

for item in items:
    
    name = item.find_element(By.CSS_SELECTOR, 'div.basicList_title__3P9Q7').text
    price = item.find_element(By.CSS_SELECTOR, 'span.price_num__2WUXn').text
    link = item.find_element(By.CSS_SELECTOR, 'div > a.basicList_link__1MaTN').get_attribute('href')
    
    print(i, name, price, link)
    
    i += 1
    
