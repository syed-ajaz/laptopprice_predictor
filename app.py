import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('reg.pkl', 'rb'))
df = pickle.load(open('file.pkl', 'rb'))
st.title("Laptop Price Predictor")
st.balloons()

processor = st.selectbox('Processor', df['Processor'].unique())
type = st.selectbox('Type', ['DDR3','DDR4','DDR5','DDR6'])
ram = st.selectbox('RAM', df['RAM'].unique())
storage = st.selectbox('Storage', df['Storage'].unique())
os = st.selectbox('OS', df['OS'].unique())

if st.button('Predict Laptop Price'):
    pre = np.array([processor, ram, storage])
    pre = pre.reshape(1,3)
    st.title("Predicted Laptop price is : " '₹'+str(int(model.predict(pre)[0])))