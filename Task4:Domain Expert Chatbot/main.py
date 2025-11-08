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
if __name__=="__main__":
    print(search_papers("computer")
