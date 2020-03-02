import os
from flask import Flask 

app= Flask(__name__)

bg_col= os.environ.get("BG_COL", "black")

@app.route('/')
def index():
    return '<h2 style="background: {};">Hello World, I am running on Python docker image</h2>'.format(bg_col);


if(__name__=="__main__"):
    app.run(host="0.0.0.0", port=1100)