from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import motion
import emotion


app=Flask(__name__)


## Route for a home page

@app.route('/')
def index():
    return render_template('homepage.html') 

@app.route('/motion_detection',methods=['GET','POST'])
def predict_motion():
    if request.method=='GET':
        return render_template('input1.html')
    else:
        _ = motion.Motion_Detection()
        res = "Done !!!"
        return render_template('input1.html',results=res)
    

@app.route('/emotion_analysis',methods=['GET','POST'])
def predict_emotion():
    if request.method=='GET':
        return render_template('input2.html')
    else:
        
        _ = emotion.get_emotions()
        res = "Done...!!!"
        
        return render_template('input2.html',results=res)
    

if __name__=="__main__":
    app.run(host="0.0.0.0")