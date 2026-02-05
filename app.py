from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#Define a rota home e renderiza
@app.route('/')
def index():
    user = {'username': 'Victor', 'email' : 'victor@gmail.com'}
    return render_template('index.html', title = 'Home', user = user)

#Define a rota form e renderiza caso o metodo for post
@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        return redirect(url_for('dashboard'))
    return render_template('form.html')

#Define a rota dashboard e renderiza
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)