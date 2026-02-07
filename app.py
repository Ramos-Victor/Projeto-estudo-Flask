from flask import Flask, render_template, request, redirect, url_for
from forms import HealthDataForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = '12345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///health_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class HealthData(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date, nullable = False)
    exercise = db.Column(db.Integer, nullable = False)
    meditation = db.Column(db.Integer, nullable = False)
    sleep = db.Column(db.Integer, nullable = False)

def __repr__(self):
    return f'<HealthData {self.id}>'

#Define a rota home e renderiza
@app.route('/')
def index():
    return render_template('index.html', title = 'Home')

#Define a rota form e renderiza caso o metodo for post
@app.route('/form', methods=['POST', 'GET'])
def form():
    
    form = HealthDataForm()
    if form.validate_on_submit():
        new_data = HealthData(
            date = form.date.data, 
            exercise = form.exercise.data, 
            meditation = form.meditation.data,
            sleep = form.sleep.data
        )

        db.session.add(new_data)
        db.session.commit()
        
        return redirect(url_for('dashboard'))
    return render_template('form.html', form=form)

#Define a rota dashboard e renderiza
@app.route('/dashboard')
def dashboard():
    all_data = HealthData.query.all()
    return render_template('dashboard.html', data=all_data)

if __name__ == '__main__':
    app.run(debug=True)