from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy import false

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<WeatherData {self.city_name} - {self.data_type}>'
