import numpy as np 
from flask import Flask,request,render_template
import vikiprocess

app = Flask(__name__)

@app.route('/')
def dynamic_page():
    return vikiprocess.show()

if __name__ == '__main__':
    app.run(debug=True)
