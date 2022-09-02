
from flask import Flask,request

app=Flask(__name__)


@app.route("/",methods=["POST"])
def home():
    return "Hello World"

@app.route("/hello")
def homeNew():
    return "Hello says hello"


app.run(debug=True,port=5000)