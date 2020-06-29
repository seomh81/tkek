import requests
from bs4 import BeautifulSoup

search_keyword = '승강기'
url = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={search_keyword}'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
news_titles = soup.select('.news .type01 li dt a[title]')

print('총', len(news_titles), '개의 뉴스 제목이 있습니다')
print()
for title in news_titles:
    print(title['title'])

"""
총 10 개의 뉴스 제목이 있습니다

[르포] 애플 심장부서 5G체험..."Z플립 만져보니 사고 싶어요"
"언팩도 생중계"...'애플 본사에서 20분 거리' 삼성전자 체험 매장 가보니
LG이노텍, 올해 애플 효과 더 커진다…아이폰에도 TOF 공급 유력
미 법원, 직원들 가방검사한 애플에 "검사 대기시간도 급여줘라"
애플 OTT '애플TV+' 한국 출시하나?…'영상사업 리더' 채용 공고
스마트폰 AS, 삼성 LG는 “고객님” 애플은 “호갱님”
스마트 스피커, '애플만 빼고' 미국·중국이 독식
[르포]“100배줌 카메라 신기해요”...애플 본고장도 놀란 갤S20·갤Z플립
한국 '영상 사업 전문가; 모집하는 애플, '애플TV 플러스' 론칭 임박?
국내 소비자 "애플, AS 불편하고 수리비 부담 커"..불만 여전
"""