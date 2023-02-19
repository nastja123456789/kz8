import pickle
import streamlit as st

# loading in the model to predict on the data
from django.shortcuts import render

pickle_in = open('./savedModels/classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)


def welcome():
    return 'welcome all'


def prediction(sepal_length, sepal_width):
    prediction = classifier.predict(
        [[sepal_length, sepal_width]])
    print(prediction)
    return prediction


def main(request):
    res = ''
    if request.method == 'POST':
        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        result = prediction(sepal_length, sepal_width)
        if result == 0:
            res = 'sacura'
        elif result == 2:
            res = 'app.py'
        else:
            res = 'look'
    return render(request, 'main.html', {'result': res})
