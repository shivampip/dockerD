import os
from flask import Flask 

app= Flask(__name__)

bg_col= os.environ.get("BG_COL", "black")

@app.route('/')
def index():
    return '<h2 style="background: {};">Hello World</h2>'.format(bg_col);


if(__name__=="__main__"):
    app.run(port=1100)