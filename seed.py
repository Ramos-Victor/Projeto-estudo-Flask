from app import db
from app import HealthData
from datetime import datetime, timedelta
import random

db.drop_all()
db.create_all()

start_date = datetime.now() - timedelta(days=90)
for i in range(90):
    date = start_date + timedelta(days = 1)
    exercise = random.randint(0,120)
    meditation = random.randint(0,60)
    sleep = random.uniform(4,10)
    data = HealthData(date = date, exercise=exercise, meditation = meditation, sleep =sleep)
    db.session.add(data)

db.session.commit()