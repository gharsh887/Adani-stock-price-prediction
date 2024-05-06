import streamlit as st
import pandas as pd
from joblib import load

model = load("model.joblib")

def predict(var1, var2, var3, var4):
    l = ['previous_day_open','previous_day_low','previous_day_close','previous_day_volume']
    s = pd.DataFrame([[var1,var2,var3,var4]],columns=l,index=None)
    prediction = model.predict(s)[0]
    return prediction

def main():
    st.title('Adani Enterprises Stock Price Prediction')

    var1 = st.number_input('Previous Day Open')
    var2 = st.number_input('Previous Day Low')
    var3 = st.number_input('Previous Day Close')
    var4 = st.number_input('Previous Day Volume')

    if st.button('Predict'):
        prediction = predict(var1, var2, var3, var4)
        st.write(f'Predicted Price: {prediction}')

if __name__ == '__main__':
    main()
