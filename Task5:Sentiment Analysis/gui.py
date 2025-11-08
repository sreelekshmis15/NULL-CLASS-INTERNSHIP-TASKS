import streamlit as st
def sentiment_stub(text):
    t=text.lower()
    if any(x in t for x in ["good","great","happy","love"]):
        return "positive"
    if any(x in t for x in ["bad","sad","hate","angry"]):
        return "negative"
    return "neutral"
st.title("Task 6: Sentiment Analysis Chatbot (Minimal GUI)")
q=st.text_input("Enter user message")
if q:
    st.write("Sentiment:",sentiment_stub(q))