#!/usr/bin/env python
# coding: utf-8

# In[16]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
from collections import Counter
from matplotlib import font_manager, rc
from wordcloud import WordCloud 
from PIL import Image 
import matplotlib
import matplotlib.pyplot as plt 

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# 실시간 코드
def cloud():
    data = pd.read_csv('hashtag.csv',delimiter=',')
    data = data.drop(['Unnamed: 0', 'date'], axis=1)
    data = data.replace("'", '', regex=True)

    l1 = []
    l2 = []

    # 문자열을 리스트로 변환
    for i in range(len(data)):
        lst = data['tag_total'][i].split(',')
        lst[0] = lst[0].replace("[", '')
        lst[-1] = lst[-1].replace("]", '')

        for j in range(len(lst)):
            lst[j] = lst[j].replace(" ", "")

        l1.append(lst)

    word = []
    # 리스트에 있는 값들을 하나의 배열로 변환
    for i in range(len(l1)):
        for j in range(len(l1[i])):
            word.append(l1[i][j])

    # 빈도 수가 1인 것 제외
    tag_counts = Counter(word)

    tag_fre = []
    tag_ct = []
    for word in tag_counts:
        if tag_counts[word] > 4:
            tag_fre.append(word)
            tag_ct.append(tag_counts[word])

    tag_data = pd.DataFrame(tag_fre)
    tag_data['count'] = tag_ct
    tag_data.columns = ['items', 'counts']
    tag_data2 = tag_data.sort_values(by=['counts'], ascending=False)

    recommend = tag_data2['items'][:30]
    recom = " ".join(recommend)
    
    plt.figure(figsize=(12,8))
    plt.title("태그 빈도")
    plt.barh(tag_data2['items'][:30],tag_data2['counts'][:30])
    plt.savefig('static/wordCloud1.png')
    plt.close()

    # icon = Image.open('icon.png')    # 마스크가 될 이미지 불러오기 

    icon = Image.open('static/img/cloud_img.png')    # 마스크가 될 이미지 불러오기 
    plt.imshow(icon)
    plt.close()

    mask = Image.new("RGB", icon.size, (255,255,255))
    mask.paste(icon,icon)
    mask = np.array(mask)

    matplotlib.rcParams['font.family'] = "Maulgun Gothic" 
    font_path="C:/Windows/Fonts/malgun.ttf" 
    wc = WordCloud(font_path=font_path, background_color="white", width=800, height=600, mask=mask) 
    cloud = wc.generate_from_frequencies(tag_counts) 
    plt.figure(figsize = (15, 12)) 
    plt.axis('off') 
    plt.imshow(cloud)
    plt.savefig('static/wordCloud2.png')
    plt.close()
    
    return recom

def cloud_pl():
    data = pd.read_csv('hashtag2.csv',delimiter=',')
    data = data.drop(['Unnamed: 0', 'date'], axis=1)
    data = data.replace("'", '', regex=True)

    l1 = []
    l2 = []

    # 문자열을 리스트로 변환
    for i in range(len(data)):
        lst = data['tag_total'][i].split(',')
        lst[0] = lst[0].replace("[", '')
        lst[-1] = lst[-1].replace("]", '')

        for j in range(len(lst)):
            lst[j] = lst[j].replace(" ", "")

        l1.append(lst)

    word = []
    # 리스트에 있는 값들을 하나의 배열로 변환
    for i in range(len(l1)):
        for j in range(len(l1[i])):
            word.append(l1[i][j])

    # 빈도 수가 1인 것 제외
    tag_counts = Counter(word)

    tag_fre = []
    tag_ct = []
    for word in tag_counts:
        if tag_counts[word] > 4:
            tag_fre.append(word)
            tag_ct.append(tag_counts[word])

    tag_data = pd.DataFrame(tag_fre)
    tag_data['count'] = tag_ct
    tag_data.columns = ['items', 'counts']
    tag_data2 = tag_data.sort_values(by=['counts'], ascending=False)

    recommend = tag_data2['items'][:30]
    recom = " ".join(recommend)
    
    plt.figure(figsize=(12,8))
    plt.title("태그 빈도")
    plt.barh(tag_data2['items'][:30],tag_data2['counts'][:30])
    plt.savefig('static/wordCloud1.png')
    plt.close()

    # icon = Image.open('icon.png')    # 마스크가 될 이미지 불러오기 

    icon = Image.open('static/img/cloud_img.png')    # 마스크가 될 이미지 불러오기 
    plt.imshow(icon)
    plt.close()

    mask = Image.new("RGB", icon.size, (255,255,255))
    mask.paste(icon,icon)
    mask = np.array(mask)

    matplotlib.rcParams['font.family'] = "Maulgun Gothic" 
    font_path="C:/Windows/Fonts/malgun.ttf" 
    wc = WordCloud(font_path=font_path, background_color="white", width=800, height=600, mask=mask) 
    cloud = wc.generate_from_frequencies(tag_counts) 
    plt.figure(figsize = (15, 12)) 
    plt.axis('off') 
    plt.imshow(cloud)
    plt.savefig('static/wordCloud2.png')
    plt.close()
    
    return recom
    
def cloud_ham():
    data = pd.read_csv('hashtag_ham.csv',delimiter=',')
    data = data.drop(['Unnamed: 0', 'date'], axis=1)
    data = data.replace("'", '', regex=True)

    l1 = []
    l2 = []

    # 문자열을 리스트로 변환
    for i in range(len(data)):
        lst = data['tag_total'][i].split(',')
        lst[0] = lst[0].replace("[", '')
        lst[-1] = lst[-1].replace("]", '')

        for j in range(len(lst)):
            lst[j] = lst[j].replace(" ", "")

        l1.append(lst)

    word = []
    # 리스트에 있는 값들을 하나의 배열로 변환
    for i in range(len(l1)):
        for j in range(len(l1[i])):
            word.append(l1[i][j])

    # 빈도 수가 1인 것 제외
    tag_counts = Counter(word)

    tag_fre = []
    tag_ct = []
    for word in tag_counts:
        if tag_counts[word] > 4:
            tag_fre.append(word)
            tag_ct.append(tag_counts[word])

    tag_data = pd.DataFrame(tag_fre)
    tag_data['count'] = tag_ct
    tag_data.columns = ['items', 'counts']
    tag_data2 = tag_data.sort_values(by=['counts'], ascending=False)

    recommend = tag_data2['items'][:30]
    recom = " ".join(recommend)
    
    plt.figure(figsize=(12,8))
    plt.title("태그 빈도")
    plt.barh(tag_data2['items'][:30],tag_data2['counts'][:30])
    plt.savefig('static/wordCloud1.png')
    plt.close()

    # icon = Image.open('icon.png')    # 마스크가 될 이미지 불러오기 

    icon = Image.open('static/img/cloud_img.png')    # 마스크가 될 이미지 불러오기 
    plt.imshow(icon)
    plt.close()

    mask = Image.new("RGB", icon.size, (255,255,255))
    mask.paste(icon,icon)
    mask = np.array(mask)

    matplotlib.rcParams['font.family'] = "Maulgun Gothic" 
    font_path="C:/Windows/Fonts/malgun.ttf" 
    wc = WordCloud(font_path=font_path, background_color="white", width=800, height=600, mask=mask) 
    cloud = wc.generate_from_frequencies(tag_counts) 
    plt.figure(figsize = (15, 12)) 
    plt.axis('off') 
    plt.imshow(cloud)
    plt.savefig('static/wordCloud2.png')
    plt.close()
    
    return recom

def cloud_ma():
    data = pd.read_csv('hashtag_ma.csv',delimiter=',')
    data = data.drop(['Unnamed: 0', 'date'], axis=1)
    data = data.replace("'", '', regex=True)

    l1 = []
    l2 = []

    # 문자열을 리스트로 변환
    for i in range(len(data)):
        lst = data['tag_total'][i].split(',')
        lst[0] = lst[0].replace("[", '')
        lst[-1] = lst[-1].replace("]", '')

        for j in range(len(lst)):
            lst[j] = lst[j].replace(" ", "")

        l1.append(lst)

    word = []
    # 리스트에 있는 값들을 하나의 배열로 변환
    for i in range(len(l1)):
        for j in range(len(l1[i])):
            word.append(l1[i][j])

    # 빈도 수가 1인 것 제외
    tag_counts = Counter(word)

    tag_fre = []
    tag_ct = []
    for word in tag_counts:
        if tag_counts[word] > 4:
            tag_fre.append(word)
            tag_ct.append(tag_counts[word])

    tag_data = pd.DataFrame(tag_fre)
    tag_data['count'] = tag_ct
    tag_data.columns = ['items', 'counts']
    tag_data2 = tag_data.sort_values(by=['counts'], ascending=False)

    recommend = tag_data2['items'][:30]
    recom = " ".join(recommend)
    
    plt.figure(figsize=(12,8))
    plt.title("태그 빈도")
    plt.barh(tag_data2['items'][:30],tag_data2['counts'][:30])
    plt.savefig('static/wordCloud1.png')
    plt.close()

    # icon = Image.open('icon.png')    # 마스크가 될 이미지 불러오기 

    icon = Image.open('static/img/cloud_img.png')    # 마스크가 될 이미지 불러오기 
    plt.imshow(icon)
    plt.close()

    mask = Image.new("RGB", icon.size, (255,255,255))
    mask.paste(icon,icon)
    mask = np.array(mask)

    matplotlib.rcParams['font.family'] = "Maulgun Gothic" 
    font_path="C:/Windows/Fonts/malgun.ttf" 
    wc = WordCloud(font_path=font_path, background_color="white", width=800, height=600, mask=mask) 
    cloud = wc.generate_from_frequencies(tag_counts) 
    plt.figure(figsize = (15, 12)) 
    plt.axis('off') 
    plt.imshow(cloud)
    plt.savefig('static/wordCloud2.png')
    plt.close()
    
    return recom




