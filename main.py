import os
from flask import Flask, render_template

app = Flask(__name__)


# ... suas rotas continuam aqui ...
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/viu')
def viu():
    return render_template('viu.html')

if __name__ == "__main__":
    # O Render passa a porta correta por essa variável de ambiente
    port = int(os.environ.get("PORT", 5000))
    # É fundamental usar o host "0.0.0.0" em vez de "127.0.0.1"
    app.run(host="0.0.0.0", port=port, debug=False)
