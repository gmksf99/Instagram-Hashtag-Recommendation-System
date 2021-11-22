#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, jsonify, render_template
from keras.models import load_model
from flask.json import JSONEncoder
import keras
import numpy as np
from PIL import Image
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.preprocessing import image
import pandas as pd
from module import date_num
from module import instar_crawling
from module import network
from module import word_cloud

model_best = load_model('model\\trainedmodel_91class.hdf5', compile=False)  # 로컬 폴더 맞춰서 수정하기

food_df = pd.read_csv('model\\food_list')  # 로컬 폴더 맞춰서 수정하기
food_df = food_df.drop('Unnamed: 0', axis=1)
food_df.columns = ['food']

food_name = []

app = Flask(__name__)

@app.route('/', methods=['get','post'])  # http://127.0.0.1:5000/
def main():
    food_name.clear
    return render_template('main.html',  image_file='img/logo.png')

@app.route('/predict', methods=['post'])
def predict():
    img = Image.open(request.files['file'].stream)
    img1 = img.resize((299, 299))
    img1 = image.img_to_array(img1)
    img1 = np.expand_dims(img1, axis=0)
    img1 = preprocess_input(img1)
    img1 = img1.reshape(1, 299, 299, 3)

    pred = model_best.predict(img1)
    index = np.argmax(pred)
    pred_value = food_df['food'][index]
   
    food_name.insert(0, pred_value)

    return '{0}'.format(pred_value)

@app.route('/member') 
def getMember():
    return render_template('member.html')

@app.route('/result') 
def getResult():
    if food_name[0] == '피자':
#         instar_crawling.crawling(food_name[0])
        date_num.date_num_pl()
        network.network_pl() # 피자
        word_cloud.cloud_pl()
        
    elif food_name[0] == '햄버거':
#         instar_crawling.crawling(food_name[0])
        date_num.date_num_ham()
        network.network_ham() # 햄버거
        word_cloud.cloud_ham()
        
    elif food_name[0] == '만두':
#         instar_crawling.crawling(food_name[0])
        date_num.date_num_ma()
        network.network_ma() # 만두
        word_cloud.cloud_ma()
        
    return render_template('result.html')

@app.route('/introduce') 
def getIntroduce():
    return render_template('introduce.html')


# In[5]:


app.run(host='127.0.0.1', port=5000, debug=True, use_reloader=True)
## Jupyter Notebook에서는 debug시 에러가 뜸


# In[ ]:




