import os
import json
import string
from datetime import datetime
from wordcloud import WordCloud, STOPWORDS
import pandas as pd

def get_wordcloud(df, key):
    with open(os.path.join("tools", "sw_fr.json"), "r", encoding='utf-8') as f:
        stopwords = json.load(f)

    comment_words = ""

    for val in df[key]:
        
        val = str(val).lower()
        
        for punc in string.punctuation:
            val = val.replace(punc, " ")
        
        # split the value
        tokens = val.split()
        
        comment_words += " ".join(tokens)+" "
    
    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='white',
                    stopwords = stopwords,
                    min_font_size = 10).generate(comment_words)

    return wordcloud

def create_df(data):
    df = pd.DataFrame({"raw": data})
    df["line"] = df.raw.apply(lambda x : x[:-2])
    df["date"] = df.raw.apply(lambda x : datetime.strptime(str(x.split("]")[0][1:-4]),'%Y-%m-%d %H:%M:%S'))
    df["user"] = df.line.apply(lambda x : x.split(" ")[3][:-1])
    df["message"] = df.line.apply(lambda x : x.split(":")[3][1:])
    df = df.drop(["line", "raw"], axis=1)
    return df