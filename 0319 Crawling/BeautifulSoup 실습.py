from bs4 import BeautifulSoup
import requests

pageNum = 1

for page in range(1, 100, 10):
    
    # Get 요청, naver 서버에 대화 시도
    response = requests.get(f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=BTS&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=49&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={page}')
    print(f'{pageNum}페이지입니다.')

    # 네이버에서 html 제공, text 메소드로 태그 내 텍스트만 추출
    html = response.text

    # html 번역 선생님으로 수프 만듬
    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.select('a.news_tit')

    for title in titles:
        art_title = title.text
        link = title.attrs['href']
        print(art_title, link)
        
    pageNum += 1