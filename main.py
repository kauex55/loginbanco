from flask import Flask, render_template, request, redirect
import csv
import os 

app = Flask(__name__)

app.config['STATIC_FOLDER'] = 'static'
app.config
if not os.path.exists('itens.csv'):
    with open('itens.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Item', 'Preço', 'Estoque'])
if not os.path.exists('usuários.csv'):
    with open('usuários.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Nome', 'Senha'])

@app.route('/') 
def home():
    return redirect('/login')

@app.route('/lista', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        item = request.form['item']
        price = float(request.form['price'])
        stock = int(request.form['stock'])
        with open('itens.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([item, price, stock])
        return redirect('/lista')
    with open('itens.csv', 'r') as f:
        itens = [row for row in csv.reader(f)]
    return render_template('index.html', itens=itens)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with open('usuários.csv', 'r') as f:
            users = [row for row in csv.reader(f)]
        for user in users:
            if user[0] == username and user[1] == password:
                return redirect('/lista')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with open('usuários.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([username, password])
        return redirect('/login')
    
if __name__ == '__main__':
    app.run(debug=True)