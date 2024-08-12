from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://neondb_owner:7NVh5GIousQl@ep-sweet-wave-a5ydk6cx.us-east-2.aws.neon.tech/neondb?sslmode=require&options=project%3Dep-sweet-wave-a5ydk6cx'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import routes

with app.app_context():
  db.create_all

if __name__ == "__main__":
  app.run(debug=True)