from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  # 크롬드라이버 자동업데이트
import time
import openpyxl
from openpyxl import Workbook


wb = Workbook()

sheet = wb.active

# 셀 너비 조정
sheet.column_dimensions['A'].width = 10
sheet.column_dimensions['B'].width = 50
sheet.column_dimensions['C'].width = 15
sheet.column_dimensions['D'].width = 50

# column명 입력
sheet.append(["순위", "상품명", "가격", "상세페이지"])


service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

browser.get("https://www.naver.com")
time.sleep(2)

browser.find_element(By.CSS_SELECTOR, 'a.nav.shop').click()
time.sleep(1)

search = browser.find_element(By.CSS_SELECTOR, 'input.co_srh_input._input')

search.send_keys('아이폰13')
search.send_keys(Keys.ENTER)

time.sleep(1)

before_h = browser.execute_script("return window.scrollY") #execute_script = 자바스크립트 명령어 실행

while True:
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
    time.sleep(1) 
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:
        break
    before_h = after_h 
    
items = browser.find_elements(By.CSS_SELECTOR, 'li.basicList_item__2XT81')

i = 1

for item in items:
    
    try:
        item.find_element(By.CSS_SELECTOR, 'span.thumbnail_sale__T-L2g').text == "핫딜"
    
    except:
        name = item.find_element(By.CSS_SELECTOR, 'div > a.basicList_link__1MaTN').text
        price = item.find_element(By.CSS_SELECTOR, 'span.price_num__2WUXn').text
        link = item.find_element(By.CSS_SELECTOR, 'div > a.basicList_link__1MaTN').get_attribute('href')
        
        sheet.append([i, name, price, link])
        
        i += 1
    
# 엑셀 파일로 저장
wb.save("iPhone13_without_hotdeal.xlsx")