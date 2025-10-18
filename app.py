import streamlit as st
import pandas as pd
import joblib

model = joblib.load('credit_risk_model.pkl')

encoder = {cols:joblib.load(f"le_{cols}_encoder.pkl") for cols in ['Age','Checking account','Credit amount','Duration','Housing','Job','Purpose','Saving accounts','Sex']}
    
st.title("Credit Risk Prediction App")

age = st.number_input("Age",min_value=18,max_value=30)
job = st.number_input("Job",min_value=0,max_value=3, value=0)
credit_amount = st.number_input("Credit amount",min_value=500,value=10000)
duration = st.number_input("Duration(months)",min_value=1,value=12)

checking_acc = st.selectbox("Checking account",options=['little','moderate','rich'])
housing = st.selectbox("Housing",options=['own','free','rent'])
saving_acc = st.selectbox("Saving accounts",options=['little','moderate','rich','quite rich'])
sex = st.selectbox("Sex",options=['male','female'])
purpose = st.selectbox("Purpose",options=['car', 'radio/TV', 'furniture/equipment', 'business', 'education',
       'repairs', 'domestic appliances', 'vacation/others'])

input_data = pd.DataFrame({
    'Age':[age],
    'Sex':[encoder['Sex'].transform([sex])[0]],
    'Job':[job],
    'Housing':[encoder['Housing'].transform([housing])[0]],
    'Saving accounts':[encoder['Saving accounts'].transform([saving_acc])[0]],
    'Checking account':[encoder['Checking account'].transform([checking_acc])[0]],
    'Credit amount':[credit_amount],
    'Duration':[duration], 
    'Purpose':[encoder['Purpose'].transform([purpose])[0]]
})

# st.write(input_data)

if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1 :
        st.success("The predicted credit risk is: Good")
    else:
        st.error("The predicted credit risk is: Bad")   
