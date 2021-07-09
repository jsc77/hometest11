from base64 import b16decode
from .utils import get_plot
from django.shortcuts import render
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from django.http import JsonResponse
from .models import *
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from datetime import datetime
import time

def home(request):
    return render(request, "home.html")
def result(request):
    data = pd.read_csv(r"C:\Users\joho10\Desktop\django\django2\hq\diabetes.csv",encoding="shift-jis")
    x = data.drop("糖尿病", axis=1)
    y = data["糖尿病"]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15)
    model = LogisticRegression()
    model.fit(x_train, y_train)
    n1 = float(request.GET.get('n1'))
    n2 = float(request.GET.get('n2'))
    n3 = float(request.GET.get('n3'))
    n4 = float(request.GET.get('n4'))
    n5 = float(request.GET.get('n5'))
    n6 = float(request.GET.get('n6'))
    n7 = float(request.GET.get('n7'))
    predictions = model.predict([[n1,n2,n3,n4,n5,n6,n7]])
    result = ""
    if predictions==[1]:
        result = "糖尿病の可能性高"
    else:
        result = "糖尿病の可能性低"
    return render(request, "home.html", {"result":result})
def index(request):
    return render(request, "index.html")
def index_result(request):
    data = pd.read_csv("USA_Housing.csv")
    data = data.drop(['Address'], axis=1)
    x = data.drop('Price', axis=1)
    y = data['Price']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.30)
    model = LinearRegression()
    model.fit(x_train, y_train)
    n1 = float(request.GET.get('n1'))
    n2 = float(request.GET.get('n2'))
    n3 = float(request.GET.get('n3'))
    n4 = float(request.GET.get('n4'))
    n5 = float(request.GET.get('n5'))
    pred = model.predict(np.array([n1, n2, n3, n4, n5]))
    pred = round(pred[0])
    price = "Price is " + str(pred)

    return render(request, "index.html", {"result2":price})
def test1(request):
    return render(request, "test1.html")
def result1(request):
    cls = joblib.load('finalized_model.sav')
    lis = []
    lis.append(request.GET['ブドウ糖'])
    lis.append(request.GET['血圧'])
    lis.append(request.GET['肌の厚さ'])
    lis.append(request.GET['インシュリン'])
    lis.append(request.GET['BMI'])
    lis.append(request.GET['糖尿病血統関数'])
    lis.append(request.GET['年齢'])
    ans = cls.predict([lis])
    return render(request, "result1.html", {'ans':ans})

df = pd.read_csv(r'C:\Users\joho10\Desktop\django\django2\hq\info1.csv')
categorical = ['a', 'b', 'c', 'd']
x = df[categorical].values
y = df['result'].values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2)
# gb_clf = GradientBoostingClassifier(n_estimators=20, learning_rate=1, max_features=2, max_depth=2,random_state=0)
# gb_clf.fit(x_train, y_train)
clf = KNeighborsClassifier(n_neighbors = 2).fit(x_train, y_train)

import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyCVyZjCw8OpnubMRGEYbffmbRbAmoe7gGs",
  "authDomain": "my-project-1590551388935.firebaseapp.com",
  "databaseURL": "https://my-project-1590551388935-default-rtdb.firebaseio.com",
  "projectId": "my-project-1590551388935",
  "storageBucket": "my-project-1590551388935.appspot.com",
  "messagingSenderId": "1059469670011",
  "appId": "1:1059469670011:web:e5430139f9b23371d754de",
  "measurementId": "G-M6Q63EEJ4Y"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()

from pushbullet import Pushbullet
API_KEY = "o.RKpdKp7sNn4OuJGgf4dyjHmuc4JjNFPw"
pb = Pushbullet(API_KEY)

def main_view(request):
    # qs = Sale.objects.all()
    # x = [x.item for x in qs]
    # y = [y.price for y in qs]
    data = pd.read_csv(r'C:\Users\joho10\Desktop\django\django2\hq\data.csv')
    # x = data['x_value']
    pred = data[categorical].values
    y = clf.predict(pred)
    for i in y:
        if i == 0:
            a = "普通"
        elif i == 1:
            a = "可能性あり"
        elif i ==2:
            a = "起きる"
    # chart = get_plot(x, y)
    data = pd.read_csv(r'C:\Users\joho10\Desktop\django\django2\hq\data2.csv')
    pred2 = data[categorical].values
    y2 = clf.predict(pred2)
    for i in y2:
        if i == 0:
            b = "普通"
        elif i == 1:
            b = "可能性あり"
        elif i ==2:
            b = "起きる"
    data = pd.read_csv(r'C:\Users\joho10\Desktop\django\django2\hq\data3.csv')
    pred2 = data[categorical].values
    y3 = clf.predict(pred2)
    for i in y3:
        if i == 0:
            c = "普通"
        elif i == 1:
            c = "可能性あり"
        elif i ==2:
            c = "起きる"
    content = {'a':a,'b':b,'c':c}
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    if a == "起きる" or a == "可能性あり":
        push = pb.push_note('確認!', "１番田中さん"+now)
        db.child("data").push({'date':now,'name':"田中",'room':"1番"})
        time.sleep(2)
    elif b == "起きる" or b == "可能性あり":
        push = pb.push_note('確認!', "2番佐藤さん"+now)
        db.child("data").push({'date':now,'name':"佐藤",'room':"2番"})
        time.sleep(2)
    elif c == "起きる" or c == "可能性あり":
        push = pb.push_note('確認!', "3番加藤さん"+now)
        db.child("data").push({'date':now,'name':"加藤",'room':"3番"})
        time.sleep(2)
    return render(request, 'main.html', content)

def simple(request):
    # import serial
    import csv
    import pandas as pd
    from random import randint

    # ser = serial.Serial('COM3', baudrate=19200)

    x_value = 0
    a = 0
    b = 0
    c = 0
    d = 0
    fieldnames = ['x_value', 'a', 'b', 'c', 'd']

    with open('data.csv', 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
    with open('data2.csv', 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
    with open('data3.csv', 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

    while True:
        with open('data.csv', 'a', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            x_value += 1
            # getdata = str(ser.readline())
            # y = getdata[1:]
            # n1 = y.replace("\\r\\n","")
            # n2 = n1.replace("'","")
            # data = list(n2.split(','))
            # info = {
            #     "x_value": x_value,
            #     "a": data[0],
            #     "b": data[1],
            #     "c": data[2],
            #     "d": data[3],
            # }
            info = {
                "x_value": x_value,
                "a": randint(0,400),
                "b": randint(0,400),
                "c": randint(0,400),
                "d": randint(0,400)
            }
            csv_writer.writerow(info)
        with open('data2.csv', 'a', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            info2 = {
                "x_value": x_value,
                "a": randint(0,400),
                "b": randint(0,400),
                "c": randint(0,400),
                "d": randint(0,400)
            }
            csv_writer.writerow(info2)
        with open('data3.csv', 'a', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            info2 = {
                "x_value": x_value,
                "a": randint(0,400),
                "b": randint(0,400),
                "c": randint(0,400),
                "d": randint(0,400)
            }
            csv_writer.writerow(info2)
            time.sleep(4)

