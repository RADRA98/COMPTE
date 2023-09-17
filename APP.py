import streamlit as st

st.title("CLIENTS BANQUE PREDICTION")
# FEATURES
st.header("Donnees du Client")
left_column, right_column = st.columns(2)
with left_column:
    Genre = st.radio("Genre", ["Male", "Female"])
    local = st.radio('Zone', ["Rural", "Urban"])
    tel = st.radio("Acces Tel", ["Yes", 'No'])

with right_column:
    age = st.number_input('Age')
    travail = st.selectbox('Travail', ['Self employed', 'Government Dependent',
                                       'Formally employed Private', 'Informally employed',
                                       'Formally employed Government', 'Farming and Fishing',
                                       'Remittance Dependent', 'Other Income',
                                       'Dont Know/Refuse to answer', 'No Income'])
    status = st.selectbox('Situation Matrimonial', ['Married/Living together', 'Widowed', 'Single/Never Married',
                                                    'Divorced/Seperated', 'Dont know'])
    formation = st.selectbox("Formation", ['Secondary education', 'No formal education',
                                           'Vocational/Specialised training', 'Primary education',
                                           'Tertiary education', 'Other/Dont know/RTA'])

import pandas as pd

x = pd.DataFrame([{'location_type': local, 'cellphone_access': tel, 'age_of_respondent': age,
                   "gender_of_respondent": Genre, "marital_status": status, "education_level": formation,
                   'job_type': travail}])

a=[["Rural", "Urban"],["Yes", 'No'],["Male", "Female"],['Married/Living together', 'Widowed', 'Single/Never Married',
                                                    'Divorced/Seperated', 'Dont know'],['Secondary education', 'No formal education',
                                           'Vocational/Specialised training', 'Primary education',
                                           'Tertiary education', 'Other/Dont know/RTA'],['Self employed', 'Government Dependent',
                                       'Formally employed Private', 'Informally employed',
                                       'Formally employed Government', 'Farming and Fishing',
                                       'Remittance Dependent', 'Other Income',
                                       'Dont Know/Refuse to answer', 'No Income']]
b = []

for j in a:
    j.sort()
    b.append({j[i]: i for i in range(0, len(j))})
k=0
for i in x:
    if i != 'bank_account' and i != 'age_of_respondent':
        x[i] = x[i].map(b[k])
        k = k + 1

import joblib


def predict(data):
   logreg=joblib.load("COMPTE.sav")
  #vec = label_encoder.fit_transform(data)
   #f=sit.fit_transform(vec)
   return logreg.predict(data)

if st.button('Prediction'):
    res = predict(x)
    if res[0] == 1:
        st.text("Le client a un compte en banque")
    else:
        st.text("PAS DE COMPTE")
