#The purpose of a route is to define the URL that will be used to access a particular function.
from app import app, db
from flask import request, jsonify
from models import Book, User

# The @app.route decorator is used to define the URL that will be used to access a particular function.
#Get all books
@app.route('/api/books', methods=['GET'])
def get_books():
  books = Book.query.all()
  return jsonify([book.book_to_json() for book in books]) #convert python objects from db (models) into json