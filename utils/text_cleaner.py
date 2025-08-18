import re  
import unicodedata

def clean_text(text):
    text = unicodedata.normalize("NFKD", text)
    text = re.sub(r"\s+" , " ", text)
    text = text.strip()
    return text