#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:30:33 2020

@author: swati
"""


import streamlit as st
import pickle
import numpy as np


model=pickle.load(open('model.pkl','rb'))

def credit_default_predict(LIMIT_BAL,EDUCATION,MARRIAGE,AGE,PAY_1,BILL_AMT1,BILL_AMT2,
       BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,
       PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6):
        input=np.array([[LIMIT_BAL,EDUCATION,MARRIAGE,AGE,PAY_1,BILL_AMT1,BILL_AMT2,
       BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,
       PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6]]).astype(np.float64)
        prediction=model.predict(input)
        return prediction


def main():
    st.title("Final Project")
    html_temp="""
    <div style="background-color:green ;padding:10px">
    <h2 style="color:white;text-align:center;">Credit Card Default Predictor </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    option=st.write("by: Swati Srivastava")
    st.header(option)
    LIMIT_BAL = st.text_input("LIMIT_BAL","Type Here")
    SEX = st.radio("SEX",('1 = Male', '2 = Female'))
    EDUCATION= st.selectbox("EDUCATION(1 = graduate school; 2 = university; 3 = high school; 4 = others)",("1", "2", "3", "4"))
    MARRIAGE= st.selectbox("MARITAL STATUS (1 = married; 2 = single; 3 = others)",("1", "2", "3"))
    AGE= st.text_input("AGE","Type Here")
    PAY_1= st.selectbox("PAY_1: represents the repayment status in September (-2 = zero balance; -1 = pay duly; 0 = minimum payment; 1 = payment delay for one month; 2 = payment delay for two months; and so on up to 8 = payment delay for eight months; 9 = payment delay for nine months and above.)", ("-2", "-1", "0", "1", "2", "3", "4", "5", "6", "7", "8"))
    Description = st.write("BILL_AMT1–BILL_AMT6: Bill statement amount {in NT dollar} BILL_AMT1 represents the bill statement amount in September; BILL_AMT2 represents the bill statement amount in August; and so on up to BILL_AMT7, which represents the bill statement amount in April.")
    BILL_AMT1= st.slider("BILL_AMT1", 0.0, 100000.0)
    BILL_AMT2= st.slider("BILL_AMT2", 0.0, 100000.0)
    BILL_AMT3= st.slider("BILL_AMT3", 0.0, 100000.0)
    BILL_AMT4= st.slider("BILL_AMT4", 0.0, 100000.0)
    BILL_AMT5= st.slider("BILL_AMT5", 0.0, 100000.0)
    BILL_AMT6= st.slider("BILL_AMT6", 0.0, 100000.0)                     
    Description_for_pay_amt = st.write("PAY_AMT1–PAY_AMT6: Amount of previous payment (NT dollar). PAY_AMT1 represents the amount paid in September; PAY_AMT2 represents the amount paid in August; and so on up to PAY_AMT6, which represents the amount paid in April.")
    PAY_AMT1= st.slider("PAY_AMT1",0.0, 100000.0)
    PAY_AMT2= st.slider("PAY_AMT2",0.0, 100000.0)
    PAY_AMT3= st.slider("PAY_AMT3",0.0, 100000.0)
    PAY_AMT4= st.slider("PAY_AMT4",0.0, 100000.0)
    PAY_AMT5= st.slider("PAY_AMT5",0.0, 100000.0)
    PAY_AMT6= st.slider("PAY_AMT6",0.0, 100000.0)
  
    safe_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> Low chances of defaulting account :Does not Require Support</h2>
       </div>
    """
    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> High chances of defaulting account : Requires Support</h2>
       </div>
    """
    if st.button("Predict"):
        output= credit_default_predict(LIMIT_BAL,EDUCATION,MARRIAGE,AGE,PAY_1,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6)
        if output>0.5:
            st.markdown(danger_html,unsafe_allow_html=True)
        else:
            st.markdown(safe_html,unsafe_allow_html=True)
if __name__=='__main__':
    main()
