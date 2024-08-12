from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    review = db.Column(db.Text, nullable=True)
    rating = db.Column(db.Integer, nullable=False)
    img_url = db.Column(db.String(200), nullable=False)

    def book_to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'review': self.review,
            'rating': self.rating,
            'imgUrl': self.img_url,
        }

class User(db.Model):
    __tablename__ = 'app_user'  # Map this model to the 'app_user' table

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def user_to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
        }
