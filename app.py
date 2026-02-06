from flask import Flask, render_template, request, redirect, url_for
from forms import HealthDataForm

app = Flask(__name__)
app.secret_key = 'supersecretkey'

#Define a rota home e renderiza
@app.route('/')
def index():
    return render_template('index.html', title = 'Home')

#Define a rota form e renderiza caso o metodo for post
@app.route('/form', methods=['POST', 'GET'])
def form():
    
    form = HealthDataForm()
    if form.validate_on_submit():
        date = form.date.data
        exercise = form.exercise.data
        meditation = form.meditation.data
        sleep = form.sleep.data
        return redirect(url_for('dashboard'))
    return render_template('form.html', form=form)

#Define a rota dashboard e renderiza
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)