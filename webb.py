import pandas as pd
import joblib
from flask import Flask,request,render_template

webapp=Flask(__name__)

model = joblib.load("model/chmodel.pkl") #loading the model 

@webapp.route('/')#starting of the program
#it should pull up the index.html right
def start():
    return render_template('index.html') 
# When Predict is clicked we have to use the data input to predict the churn yay or nay
def yay_nay():
    return 
    #will write the code for this latereak
 