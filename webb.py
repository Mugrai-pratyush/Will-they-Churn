import pandas as pd
import joblib
from flask import Flask,request,render_template

webapp=Flask(__name__)

model = joblib.load("model/chmodel.pkl")