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
    try:
        input_stream= {#input from the front-end
            'gender': request.form['gender'],
            'SeniorCitizen': int(request.form['SeniorCitizen']),
            'Partner': request.form['Partner'],
            'Dependents': request.form['Dependents'],
            'tenure': int(request.form['tenure']),
            'PhoneService': request.form['PhoneService'],
            'InternetService': request.form['InternetService'],
            'Contract': request.form['Contract'],
            'PaperlessBilling': request.form['PaperlessBilling'],
            'PaymentMethod': request.form['PaymentMethod'],
            'MonthlyCharges': float(request.form['MonthlyCharges']),
            'TotalCharges': float(request.form['TotalCharges'])
        }
        input_stream = pd.DataFrame([input_stream])

        # One-hot encode just like training
        input_df_encoded = pd.get_dummies(input_stream)

        # Align with model's expected columns
        model_columns = joblib.load('model/model_columns.pkl')  # Optional: save columns during training
        input_df_encoded = input_df_encoded.reindex(columns=model_columns, fill_value=0)

        # Predict
        prediction = model.predict(input_df_encoded)[0]

        return render_template('index.html', prediction=prediction)

    except Exception as e:
        return f"Error: {e}" 
    #will write the code for this later
if __name__ == '__main__':
    webapp.run(debug=True)
 