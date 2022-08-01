import requests
from bs4 import BeautifulSoup

def crawler(keyword):
    for i in range(1):
        for j in range (30):
            try:
                link = f'https://s.search.naver.com/p/review/search.naver?rev=44&where=view&api_type=11&start={1 + 30 *i}&query={keyword}&nso=&nqx_theme=|"theme":|"main":|"name":"restaurant_list">>>&main_q=&mode=normal&q_material=&ac=0&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=31&sm=tab_jum&ssc=tab.view.view&ngn_country=KR&lgl_rcode=02630250&fgn_region=&fgn_city=&lgl_lat=37.7950756&lgl_long=126.9855156&abt=&_callback=viewMoreContents'
                link_1 = link.replace('|', '{')
                link_2 = link_1.replace('>', '}')
                naver = requests.get(link_2)
            
                soup = BeautifulSoup(naver.text.replace('\\', ''), 'html.parser')
                

                blogger = soup.select('a.sub_txt.sub_name')[j].text
                title = soup.select('.api_txt_lines.total_tit._cross_trigger')[j].text
                link = soup.select('.api_txt_lines.total_tit._cross_trigger')[j]

                csv = open(f'{keyword}.csv', 'a', encoding='cp949')
                csv.write(blogger.replace(',', '') + ',' + title.replace(',', '') + ',' + link['href'] + '\n')
                csv.close()
            except:
                pass

#리스트 안에 키워드를 채워 넣으면 됩니다
list = []

for i in list:
    crawler(i)