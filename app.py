# app.py

from flask import Flask, render_template, request
from simulation import run_simulation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    result = run_simulation()
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
