from distutils.log import debug
import string
from flask import Flask, render_template
from transformers import (
    AutoTokenizer,
    pipeline
)
app = Flask(__name__)
summarizer = pipeline("summarization")
article = """
Happy womens day to all the females in this comment section!

Also once again loved your video mysticat, keep growing your channel with your amazing content, I have a suggestion, can you make these cursed things into a datapack, like just run one command and see the magic happening and armor stands spawning!, you could even customise it for all shapes, like you accidentally did for the hexagon!
I would really love to try the circle and this triangle, and even the shark, but Im too dumb too successfully copy you lol
"""



@app.route('/')
def home():
    return getSummary(article)

@app.route("/<article>")
def summary_page(article):
    return getSummary(article);

def getSummary(article:string) -> string:
    summary = summarizer(article, max_length=24, min_length=24, do_sample=False);
    return summary[0]["summary_text"]
    
if (__name__ == "__main__"):
    app.run(debug=True)
