import pandas as pd
import numpy as n
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from PIL import Image
import PIL.ImageOps

X,y=fetch_openml('mnist_784',version=1,return_X_y=True)
xtrain,xtest,ytrain,ytest=train_test_split(X,y,random_state=9,train_size=7500,test_size=2500)
xtrains=xtrain/255.0
xtests=xtest/225.0
lr=LogisticRegression(solver="saga",multi_class='multinomial').fit(xtrains,ytrain)
def getprediction(image):
    img=Image.open(image)
    imgbw=img.covert('L')
    imgbwresize=imgbw.resize((28,28),Image.ANTIALIAS)
    pixel=20
    min_pixel=n.percentile(imgbwresize,pixel)
    imginvert=n.clip(imgbwresize-min_pixel,0,255)
    max_pixel=n.max(imgbwresize)
    imginvert=n.asarray(imginvert)/max_pixel
    testsample=n.array(imginvert).reshape(1,784)
    prediction=lr.predict(testsample)
    return prediction[0]
