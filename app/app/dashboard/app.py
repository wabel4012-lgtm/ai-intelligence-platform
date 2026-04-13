import streamlit as st
import requests

st.title("AI Intelligence Platform Dashboard")

if st.button("Test AI Evaluation"):
    res = requests.post("http://localhost:8000/evaluate", json={
        "correctness": 0.9,
        "reasoning": 0.8,
        "clarity": 0.9,
        "completeness": 0.85,
        "instruction": 0.9
    }).json()

    st.write(res)
