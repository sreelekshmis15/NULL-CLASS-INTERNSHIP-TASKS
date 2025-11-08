def sentiment_stub(text):
    t=text.lower()
    if any(x in t for x in ["good","great","happy","love"]):
        return "positive"
    if any(x in t for x in ["bad","sad","hate","angry"]):
        return "negative"
    return "neutral"
if __name__=="__main__":
    print(sentiment_stub("I am very happy"))