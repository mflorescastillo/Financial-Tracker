from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import csv

app = Flask(__name__)
CORS(app)

# Configure PostgreSQL database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/financial-tracker'
db = SQLAlchemy(app)

class CarPrice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

@app.route('/')
def home():
    return "Welcome to the Car Price Tracker API!"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    
    content = file.read().decode('utf-8')
    csv_reader = csv.reader(content.splitlines())
    
    for row in csv_reader:
        # Assuming the CSV columns are: make, model, price
        car = CarPrice(make=row[0], model=row[1], price=float(row[2]))
        db.session.add(car)
    db.session.commit()

    return "File processed", 200

if __name__ == "__main__":
    app.run(debug=True)