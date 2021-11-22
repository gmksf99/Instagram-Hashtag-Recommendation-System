#!/usr/bin/env python
# coding: utf-8

# In[134]:


"""선교.ipynb

네트워크 분석

"""
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
from tqdm import tqdm
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt 
from matplotlib import rc
import matplotlib.font_manager as fm
import numpy as np

font_name = fm.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# 실시간 코드
def network():
    # csv파일을 불러오면 리스트가 하나의 문자열이 되기 때문에 바꿔줘야 연관분석이 가능
    data = pd.read_csv('hashtag_ham.csv',delimiter=',')
    data = data.drop(['Unnamed: 0', 'date'], axis=1)
    data = data.replace("'", '', regex=True)
    
    l1 = []
    l2 = []
    for i in range(len(data)):
        lst = data['tag_total'][i].split(',')
        lst[0] = lst[0].replace("[", '')
        lst[-1] = lst[-1].replace("]", '')

        for j in range(len(lst)):
            lst[j] = lst[j].replace(" ", "")

        l1.append(lst)

    l2.append(l1)
    
    df = pd.DataFrame(l2)
    df = df.T
    df= df.replace(" ", "")
    df.columns = ['tag']
    
    te = TransactionEncoder()
    te_ary = te.fit(df['tag']).transform(df['tag'])
    df = pd.DataFrame(te_ary, columns=te.columns_)
        
    # 연관규칙
    # transactions 으로 변환
    frequent_itemsets = apriori(df, min_support = 0.1, use_colnames=True)
    
    null = []
    for i in range(len(frequent_itemsets)):
        if len(frequent_itemsets['itemsets'][i]) < 2 :
            null.append(frequent_itemsets.index[i])
    
    frequent = frequent_itemsets.drop(frequent_itemsets.index[null])

    # 항목이 2개고 지지도가 0.05이상인 것만
    frequent['len'] = frequent['itemsets'].apply(lambda x: len(x))
    frequent = frequent[(frequent['len']==2)].sort_values(by='support', ascending=False)
    ### frequent : 네트워크 분석을 위해###
    
    # 그래프 생성
    G = nx.DiGraph()
    ar = (frequent['itemsets'])
    G.add_edges_from(ar)

    # 페이지 랭크 : 노드 색상과 크기 지정
    pr = nx.pagerank(G)
    nsize = np.array([v for v in pr.values()])
    nsize = 3000 * (nsize-min(nsize)) / (max(nsize) - min(nsize))

    # 레이아웃
    # pos = nx.circular_layout(G)
    pos = nx.shell_layout(G)
    # pos = nx.kamada_kawai_layout(G)
    # pos = nx.random_layout(G)
    # pos = nx.planar_layout(G)
    # pos = nx.spring_layout(G)
    # pos = fruchterman_reingold_layout(G)

    # 그래프 그리기
    plt.figure(figsize=(9,7))
    plt.axis('off')
    nx.draw_networkx(G, font_family=font_name , font_size=16, pos=pos, node_color=list(pr.values()), 
                     node_size=5000, alpha=0.7, edge_color='.100', cmap=plt.cm.YlGn)
    plt.savefig('static/network.png')
    plt.close()

def network_pl():
    data = pd.read_csv('hashtag2.csv',delimiter=',')
    data = data.drop(['Unnamed: 0', 'date'], axis=1)
    data = data.replace("'", '', regex=True)
    
    l1 = []
    l2 = []
    for i in range(len(data)):
        lst = data['tag_total'][i].split(',')
        lst[0] = lst[0].replace("[", '')
        lst[-1] = lst[-1].replace("]", '')

        for j in range(len(lst)):
            lst[j] = lst[j].replace(" ", "")

        l1.append(lst)

    l2.append(l1)
    
    df = pd.DataFrame(l2)
    df = df.T
    df= df.replace(" ", "")
    df.columns = ['tag']
    
    te = TransactionEncoder()
    te_ary = te.fit(df['tag']).transform(df['tag'])
    df = pd.DataFrame(te_ary, columns=te.columns_)
        
    # 연관규칙
    # transactions 으로 변환
    frequent_itemsets = apriori(df, min_support = 0.1, use_colnames=True)
    
    null = []
    for i in range(len(frequent_itemsets)):
        if len(frequent_itemsets['itemsets'][i]) < 2 :
            null.append(frequent_itemsets.index[i])
    
    frequent = frequent_itemsets.drop(frequent_itemsets.index[null])

    # 항목이 2개고 지지도가 0.05이상인 것만
    frequent['len'] = frequent['itemsets'].apply(lambda x: len(x))
    frequent = frequent[(frequent['len']==2)].sort_values(by='support', ascending=False)
    ### frequent : 네트워크 분석을 위해###
    
    # 그래프 생성
    G = nx.DiGraph()
    ar = (frequent['itemsets'])
    G.add_edges_from(ar)

    # 페이지 랭크 : 노드 색상과 크기 지정
    pr = nx.pagerank(G)
    nsize = np.array([v for v in pr.values()])
    nsize = 3000 * (nsize-min(nsize)) / (max(nsize) - min(nsize))

    # 레이아웃
    # pos = nx.circular_layout(G)
    pos = nx.shell_layout(G)
    # pos = nx.kamada_kawai_layout(G)
    # pos = nx.random_layout(G)
    # pos = nx.planar_layout(G)
    # pos = nx.spring_layout(G)
    # pos = fruchterman_reingold_layout(G)

    # 그래프 그리기
    plt.figure(figsize=(9,7))
    plt.axis('off')
    nx.draw_networkx(G, font_family=font_name , font_size=16, pos=pos, node_color=list(pr.values()), 
                     node_size=5000, alpha=0.7, edge_color='.100', cmap=plt.cm.YlGn)
    plt.savefig('static/network.png')
    plt.close()
    
def network_ham():
    # csv파일을 불러오면 리스트가 하나의 문자열이 되기 때문에 바꿔줘야 연관분석이 가능
    data = pd.read_csv('hashtag_ham.csv',delimiter=',')
    data = data.drop(['Unnamed: 0', 'date'], axis=1)
    data = data.replace("'", '', regex=True)
    
    l1 = []
    l2 = []
    for i in range(len(data)):
        lst = data['tag_total'][i].split(',')
        lst[0] = lst[0].replace("[", '')
        lst[-1] = lst[-1].replace("]", '')

        for j in range(len(lst)):
            lst[j] = lst[j].replace(" ", "")

        l1.append(lst)

    l2.append(l1)
    
    df = pd.DataFrame(l2)
    df = df.T
    df= df.replace(" ", "")
    df.columns = ['tag']
    
    te = TransactionEncoder()
    te_ary = te.fit(df['tag']).transform(df['tag'])
    df = pd.DataFrame(te_ary, columns=te.columns_)
        
    # 연관규칙
    # transactions 으로 변환
    frequent_itemsets = apriori(df, min_support = 0.1, use_colnames=True)
    
    null = []
    for i in range(len(frequent_itemsets)):
        if len(frequent_itemsets['itemsets'][i]) < 2 :
            null.append(frequent_itemsets.index[i])
    
    frequent = frequent_itemsets.drop(frequent_itemsets.index[null])

    # 항목이 2개고 지지도가 0.05이상인 것만
    frequent['len'] = frequent['itemsets'].apply(lambda x: len(x))
    frequent = frequent[(frequent['len']==2)].sort_values(by='support', ascending=False)
    ### frequent : 네트워크 분석을 위해###
    
    # 그래프 생성
    G = nx.DiGraph()
    ar = (frequent['itemsets'])
    G.add_edges_from(ar)

    # 페이지 랭크 : 노드 색상과 크기 지정
    pr = nx.pagerank(G)
    nsize = np.array([v for v in pr.values()])
    nsize = 3000 * (nsize-min(nsize)) / (max(nsize) - min(nsize))

    # 레이아웃
    # pos = nx.circular_layout(G)
    pos = nx.shell_layout(G)
    # pos = nx.kamada_kawai_layout(G)
    # pos = nx.random_layout(G)
    # pos = nx.planar_layout(G)
    # pos = nx.spring_layout(G)
    # pos = fruchterman_reingold_layout(G)

    # 그래프 그리기
    plt.figure(figsize=(9,7))
    plt.axis('off')
    nx.draw_networkx(G, font_family=font_name , font_size=16, pos=pos, node_color=list(pr.values()), 
                     node_size=5000, alpha=0.7, edge_color='.100', cmap=plt.cm.YlGn)
    plt.savefig('static/network.png')
    plt.close()

def network_ma():
    # csv파일을 불러오면 리스트가 하나의 문자열이 되기 때문에 바꿔줘야 연관분석이 가능
    data = pd.read_csv('hashtag_ma.csv',delimiter=',')
    data = data.drop(['Unnamed: 0', 'date'], axis=1)
    data = data.replace("'", '', regex=True)
    
    l1 = []
    l2 = []
    for i in range(len(data)):
        lst = data['tag_total'][i].split(',')
        lst[0] = lst[0].replace("[", '')
        lst[-1] = lst[-1].replace("]", '')

        for j in range(len(lst)):
            lst[j] = lst[j].replace(" ", "")

        l1.append(lst)

    l2.append(l1)
    
    df = pd.DataFrame(l2)
    df = df.T
    df= df.replace(" ", "")
    df.columns = ['tag']
    
    te = TransactionEncoder()
    te_ary = te.fit(df['tag']).transform(df['tag'])
    df = pd.DataFrame(te_ary, columns=te.columns_)
        
    # 연관규칙
    # transactions 으로 변환
    frequent_itemsets = apriori(df, min_support = 0.1, use_colnames=True)
    
    null = []
    for i in range(len(frequent_itemsets)):
        if len(frequent_itemsets['itemsets'][i]) < 2 :
            null.append(frequent_itemsets.index[i])
    
    frequent = frequent_itemsets.drop(frequent_itemsets.index[null])

    # 항목이 2개고 지지도가 0.05이상인 것만
    frequent['len'] = frequent['itemsets'].apply(lambda x: len(x))
    frequent = frequent[(frequent['len']==2)].sort_values(by='support', ascending=False)
    ### frequent : 네트워크 분석을 위해###
    
    # 그래프 생성
    G = nx.DiGraph()
    ar = (frequent['itemsets'])
    G.add_edges_from(ar)

    # 페이지 랭크 : 노드 색상과 크기 지정
    pr = nx.pagerank(G)
    nsize = np.array([v for v in pr.values()])
    nsize = 3000 * (nsize-min(nsize)) / (max(nsize) - min(nsize))
    font_name = fm.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)

    # 레이아웃
    # pos = nx.circular_layout(G)
    pos = nx.shell_layout(G)
    # pos = nx.kamada_kawai_layout(G)
    # pos = nx.random_layout(G)
    # pos = nx.planar_layout(G)
    # pos = nx.spring_layout(G)
    # pos = fruchterman_reingold_layout(G)

    # 그래프 그리기
    plt.figure(figsize=(9,7))
    plt.axis('off')
    nx.draw_networkx(G, font_family=font_name , font_size=16, pos=pos, node_color=list(pr.values()), 
                     node_size=5000, alpha=0.7, edge_color='.100', cmap=plt.cm.YlGn)
    plt.savefig('static/network.png')
    plt.close()
