from flask import Flask, request

import joblib

application=Flask(__name__)

vectorizer= joblib.load("vectorizer.pkl")
spamorham_model=joblib.load("spam_ham_model.pkl")

@application.route('/')
def hello_world():
    return "Hello World"

@application.route('/spamorham')


def spamorham():
    message=request.args.get("message")
    vect_message=vectorizer.transform([message])
    result=spamorham_model.predict(vect_message)[0]
    return result
    
if __name__ == '__main__':
   application.run()
