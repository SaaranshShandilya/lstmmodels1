from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import nltk
import tensorflow
from nltk.corpus import stopwords
from nltk import word_tokenize
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import re
nltk.download('stopwords')
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

STOPWORDS = set(stopwords.words('english'))
REPLACE_BY_SPACE_RE = re.compile('[/(){}\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')

MAX_NB_WORDS = 50000
MAX_SEQUENCE_LENGTH = 250

tokenizer = Tokenizer(num_words=MAX_NB_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)
model_q1 = tensorflow.keras.models.load_model('lstm/Q1LSTM.hdf5')
model_q2 = tensorflow.keras.models.load_model('lstm/Q2LSTM.hdf5')
model_q3 = tensorflow.keras.models.load_model('lstm/Q3LSTM.hdf5')
model_q4 = tensorflow.keras.models.load_model('lstm/Q4LSTM.hdf5')
model_q5 = tensorflow.keras.models.load_model('lstm/Q5LSTM.hdf5')
model_q6 = tensorflow.keras.models.load_model('lstm/Q6LSTM.hdf5')
model_q7 = tensorflow.keras.models.load_model('lstm/Q7LSTM.hdf5')
model_q8 = tensorflow.keras.models.load_model('lstm/Q8LSTM.hdf5')
rank = ['Bad', 'Below Average', 'Average', 'Above Average', 'Good']




@csrf_exempt
def home(request):

    body = json.loads(request.body.decode('utf-8'))
    text = body['text']
    ques = body['ques']
    # print(new_text)
    test = []
    test.append(text)
    print(test)
    tokenizer.fit_on_texts(test)
    seq = tokenizer.texts_to_sequences(test)
    padded = pad_sequences(seq, maxlen=MAX_SEQUENCE_LENGTH)
    if(ques == 1):
        pred = model_q1.predict(padded)
    elif(ques == 2):
        pred = model_q2.predict(padded) 
    elif(ques == 3):
        pred = model_q3.predict(padded)
    elif(ques == 4):
        pred = model_q4.predict(padded)
    elif(ques == 5):
        pred = model_q5.predict(padded)    
    elif(ques == 6):
        pred = model_q5.predict(padded)  
    elif(ques == 7):
        pred = model_q5.predict(padded)    
    elif(ques == 8):
        pred = model_q5.predict(padded)    
       
    print(seq)
    print(pred, rank[np.argmax(pred)])
    ranking = rank[np.argmax(pred)]
    print(ranking)
    return JsonResponse({'status':"succes","rank":ranking})

# Create your views here.
