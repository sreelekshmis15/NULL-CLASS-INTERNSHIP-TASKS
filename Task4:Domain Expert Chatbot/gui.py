import streamlit as st
from pathlib import Path
import json
def load_papers(path="papers.json"):
    p=Path(path)
    if p.exists():
        return json.load(p.open())
    return {"papers":[{"title":"Example Paper","abstract":"This is an example abstract about computer science."}]}
def search_papers(query):
    data=load_papers()
    res=[]
    for p in data.get("papers",[]):
        if query.lower() in p.get("abstract","").lower() or query.lower() in p.get("title","").lower():
            res.append(p)
    return res
st.title("Task 5: Domain-Expert Chatbot (Minimal GUI)")
q=st.text_input("Search papers or ask a topic")
if q:
    hits=search_papers(q)
    if hits:
        for h in hits:
            st.write(h.get("title"))
            st.write(h.get("abstract"))
    else:
        st.write("No direct matches found. Integrate retrieval+LLM for full answers.")