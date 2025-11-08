def detect_language_stub(text):
    return "en"
def translate_stub(text,target="en"):
    return text
def respond(text):
    lang=detect_language_stub(text)
    return f"Detected {lang}. Response (stub): I received '{text}'"
if __name__=="__main__":
    print(respond("Hola"))