import numpy as np
import pickle
import pandas as pd
import streamlit as st
rg = pickle.load(open("nepal_corona_predictor.pkl",'rb'))
def welcome():
    return "Welcome All"
def corona_case_predictor(total_cases,total_deaths,new_deaths,new_tests,total_tests,year):
    prediction = rg.predict([[total_cases,total_deaths,new_deaths,new_tests,total_tests,year]])
    return prediction[0].round(0)
def main():
    st.title("Nepal New Corona Case Predictor")
    html_temp="""
    <div style="background-color:orange;padding:10px">
    <h2 style="color:white'text-align:center;">Streamlit Nepal New Case Predictor ML App</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    total_cases = st.text_input("Total_Cases","Type Here")
    total_deaths = st.text_input("Total_Deaths","Type Here")
    new_deaths = st.text_input("New_Deaths","Type Here")
    new_tests = st.text_input("New_Tests","Type Here")
    total_tests = st.text_input("Total_Tests","Type Here")
    year = st.text_input("Year","Type Here")
    result=""
    if st.button("Predict"):
        result = corona_case_predictor(total_cases,total_deaths,new_deaths,new_tests,total_tests,year)
    st.success(result)
    if st.button("About"):
        st.text("Nepal_Corona_New_Case_Predictor")
        st.text("Project for Machine Learning")
        st.text("© SantoshThapa 2020")
    
if __name__=='__main__':
    main()