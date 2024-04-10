from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    return render_template('register.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

if __name__ == '__main__':
    app.run(debug=True)