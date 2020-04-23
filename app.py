import numpy as np 
from flask import Flask,request,render_template
import vikiprocess

app = Flask(__name__)

@app.route('/')
def dynamic_page():
    return vikiprocess.show()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8000', debug=True)
