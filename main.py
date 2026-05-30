from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/viu')
def viu():
    return render_template('viu.html')
app.run(debug=True)