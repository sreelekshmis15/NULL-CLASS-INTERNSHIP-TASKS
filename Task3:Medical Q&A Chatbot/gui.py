import streamlit as st
from pathlib import Path
import json
def load_faq(path="medical_faq.json"):
    p=Path(path)
    if p.exists():
        return json.load(p.open())
    return {"qa":[{"q":"What is fever?","a":"Fever is elevated body temperature."}]}
def simple_answer(question):
    data=load_faq()
    for item in data.get("qa",[]):
        if item["q"].lower() in question.lower() or question.lower() in item["q"].lower():
            return item["a"]
    return "No exact match found. Replace with a retrieval model for production."
st.title("Task 3: Medical QA Chatbot (Minimal GUI)")
q=st.text_input("Ask a medical question")
if q:
    st.write(simple_answer(q))