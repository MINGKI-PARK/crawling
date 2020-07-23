
# 이거하면 셀을 파일로 저장해줌!!!!!

import re
import requests
from urllib import parse
from bs4 import BeautifulSoup

def get_daumnews_info(url):
    '''
    [파라미터]
        url : 다음 기사 url
    [반환값]
        tuple : (제목, 기자이름, 입력일, 기사내용)
    '''
    res = requests.get(url)
    
    if res.status_code == 200:
        soup = BeautifulSoup(res.text)
        
        title_tag = soup.select_one('h3.tit_view')
        reporter_tag = soup.select_one('span.info_view span.txt_info:nth-child(1)')
        input_date_tag = soup.select_one('span.info_view span.txt_info:nth-child(2)')
        news_tag = soup.select_one('div#harmonyContainer')
        
        # 파인드나 셀렉트를 하게되면 태그 객체가 반환된다.
        
        return title_tag.text.strip(), reporter_tag.text.strip(), input_date_tag.text.strip(), re.sub(r'\s+', ' ', news_tag.text.strip())
    
        # 공백 없애기 위해서 스트립을 많이 붙여준다. 특히 문자열이나 텍스트에 많이 붙여줌.
        
        # 정규 표현식 공부해야겠다 다시.
    
    else:
        raise Exception('요청 결과를 가져오지 못했습니다. 에러코드 : {}'.format(res.status_code))
        
        
