#!/usr/bin/env python
# coding: utf-8

# In[3]:


from selenium import webdriver
from urllib.parse import quote_plus
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os
import pandas as pd
import unicodedata
import re


# In[39]:


def crawling(tag):
    search_word = tag
    tag_n = 10
    
    # 브라우저를 기동X, 백그라운드에서 작업 수행
    options = webdriver.ChromeOptions()
    
    # 인스타 경우 백그라운드에서 css, xpath가 검색이 안됨 ㅠㅜ
#     options.add_argument('--headless')
#     options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1280x1024')
    
    driver = webdriver.Chrome('chromedriver', options=options)
    action = ActionChains(driver)

    url = 'https://www.instagram.com/accounts/login/'

    driver.get(url)
    
    ############인스타그램 오픈 준비###################

    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('gmksf99@naver.com')
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('gmksf409!!')

    xpath = '//*[@id="loginForm"]/div/div[3]/button'
    driver.find_element_by_xpath(xpath).click()
    time.sleep(3)

    driver.get('https://www.instagram.com/explore/tags/' + search_word)

    ############# #####자동로그인까지###################
    tag_id = []
    tag_all = []
    n=1
    time2 = []
    tag_list2=[] # 첫 게시글만 사용

    time.sleep(8)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]').click()
    asd = '/html/body/div[6]/div[2]/div/article/div[3]/div[1]/ul/div/li/div/div/div[2]/span/a'
    asd2 = '/html/body/div[6]/div[2]/div/article/div[3]/div[2]/a/time'

    time.sleep(5)
    tags1 = driver.find_elements_by_xpath(asd)
    tags2 = driver.find_element_by_xpath(asd2)

#     # 인기게시글 넘어감
#     driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a').click()
#     driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a').click()
#     driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a').click()

#     driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a').click()
#     driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a').click()
#     driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a').click()


#     driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a').click()
#     driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a').click()
#     driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a').click()

    time.sleep(5)
    while True :
        try:
            if int(tag_n) > n:
                tag_list=[]
                tags1 = []
                tags2 = ''

                driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/a[2]').click()
                driver.implicitly_wait(5)

                tags1 = driver.find_elements_by_xpath(asd)
                tags2 = driver.find_element_by_xpath(asd2)

                #print("시간", tags2.get_attribute("datetime"), "------------------")
                for j in tags1:
                    #print(n)
                    #print(j.text)
                    tag_list.append(j.text)
                    tag_all.append(j.text)
                    n += 1

                tag_id.append(tag_list)
                time2.append(tags2.get_attribute("datetime"))

    #             for n2 in range(3):
    #                 driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]').click()
    #                 time.sleep(5)
    #                 print(n2)

    #                 if(n2 == 2):
    #                     tags1 = driver.find_elements_by_xpath(asd)
    #                     tags2 = driver.find_element_by_xpath(asd2)

    #                     print("시간", tags2.text, "------------------")
    #                     for j in tags1:
    #                         print(n)
    #                         print(j.text)
    #                         tag_list.append(j.text)
    #                         tag_all.append(j.text)
    #                         n += 1

    #                     tag_id.append(tag_list)
    #                     time2.append(tags2.get_attribute("datetime"))  

            else:
                if n >= int(tag_n):
                    break

                else:
                    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

        except:
            if n >= int(tag_n):
                break
    ########해당개수만큼 해시태그 불러오기까지########
    
    # 데이터 프레임으로 저장
    tag_df = pd.DataFrame()
    tag_df['tag_total'] = tag_id
    tag_df['date'] = time2
    
    # 한글깨짐 방지 함수 사용
    tag_df = uni(tag_df)
    # 널값 제거
    tag_drop = null_value(tag_df)
    # 중복리스트 제거
    tag_drop2 = double(tag_drop)
    # 특수문자 제거
    tag_drop2 = patten(tag_drop2)
    # 널값 제거(재확인) _ 사실 널값 제거를 맨 마지막 한번만 해도 될듯(혹시 모르니)
    instar_df = null_value(tag_drop2)
    
    # 데이터 저장
    instar_df.to_csv('hashtag.csv', encoding='utf-8-sig')
    print("저장완료!")


# In[19]:


# 한글깨짐 방지
def uni(tag_df):
    t = []
    for i in range(len(tag_df)):
        new = []
        for j in range(len(tag_df['tag_total'][i])):
            text = tag_df['tag_total'][i][j]  
            t_new = unicodedata.normalize('NFC', text)
            new.append(t_new)
        t.append(new)

    tag_df['tag_total'] = t
    return tag_df

# 널값 제거
def null_value(tag_df):
    null = []
    for i in range(len(tag_df)):
        if len(tag_df['tag_total'][i]) < 3 :
            null.append(tag_df.index[i])

    tag_drop = tag_df.drop(tag_df.index[null])
    tag_drop.reset_index(drop=True, inplace=True)
    return tag_drop

# 중복리스트(광고) 제거
def double(tag_drop):
    null2 = []
    for i in range(len(tag_drop)):
        for j in range(len(tag_drop)):
            if i != j :
                if tag_drop['tag_total'][i] == tag_drop['tag_total'][j]:
                    null2.append(tag_drop.index[i])
                    break
                    
    tag_drop2 = tag_drop.drop(tag_drop.index[null2])
    tag_drop2.reset_index(drop=True, inplace=True)
    return tag_drop2

# 특수문자 제거(+숫자)
def patten(tag_drop2):
    tag_clean = [] # 게시글 형태로 저장
    tag_co = [] # 태그 별로 저장
    emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
            u"^0-9$"    
            u"-=+,/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》"  "]+", flags=re.UNICODE)

    for i in range(len(tag_drop2)):
        t = []
        for j in range(len(tag_drop2['tag_total'][i])):
            text = tag_drop2['tag_total'][i][j]
            parse = emoji_pattern.sub(r'', text) # no emoji
            if parse != '' and parse != '#':
                t.append(parse)
                tag_co.append(parse) # 빈도수때 사용

        tag_clean.append(t)

    tag_drop2['tag_total'] = tag_clean
    return tag_drop2




