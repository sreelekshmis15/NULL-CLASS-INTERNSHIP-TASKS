import os
import json
def load_knowledge(kb_path="knowledge.json"):
    if os.path.exists(kb_path):
        with open(kb_path,"r") as f:
            return json.load(f)
    return {"documents":[]}
def add_knowledge(text,kb_path="knowledge.json"):
    kb=load_knowledge(kb_path)
    kb["documents"].append({"text":text})
    with open(kb_path,"w") as f:
        json.dump(kb,f,indent=2)
def query_stub(q):
    return "This is a stubbed response. Replace with an embedding+vector DB retrieval."
if __name__=="__main__":
    kb="knowledge.json"
    add_knowledge("Example knowledge added programmatically",kb)
    print(query_stub("What is in the KB?"))