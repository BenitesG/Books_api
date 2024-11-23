import mysql.connector
from flask import Flask, jsonify, request

# API CRUD

mydb = mysql.connector.connect(
    host='CHANGE-ME',
    user='CHANGE-ME',
    password='CHANGE-ME',
    database='CHANGE-ME',
)

app = Flask(__name__)

# Create (C)
@app.route('/books',methods=['POST'])
def create_new_book():
    new_book = request.get_json()
    
    # Insert data
    cursor = mydb.cursor() 
    sql = f"INSERT INTO books (title, writer) VALUES ('{new_book['title']}', '{new_book['writer']}')"
    cursor.execute(sql)
    mydb.commit()
     
    return jsonify(new_book)

# Search(All) (R)
@app.route('/books',methods=['GET'])
def get_books():

    # Show all books
    cursor = mydb.cursor()
    sql = f'SELECT * FROM books'
    cursor.execute(sql)
    my_books = cursor.fetchall()

    # Data processing
    books = list()
    for book in my_books:
        books.append(
            {
                'id': book[0], # type: ignore
                'title': book[1], # type: ignore
                'writer': book[2]  # type: ignore
            }
        )

    return jsonify(books)

# Search(ID) (R)
@app.route('/books/<int:id>',methods=['GET']) 
def get_book_by_id(id):

    # Shows books by given id
    cursor = mydb.cursor()
    sql = f'SELECT * FROM books WHERE id = %s;'
    cursor.execute(sql, (id,))
    book = cursor.fetchone()
    
    # No number sent in id
    if not isinstance(id, int):
        return jsonify({'error': 'Invalid ID.'}), 400
    
    # Data processing
    if book:
        return jsonify(
            {
                'id': book[0], # type: ignore
                'title': book[1], # type: ignore
                'writer': book[2] # type: ignore
            }
        )
    else:
        return jsonify({'error': 'Book not found!'}), 404
        
# Edit (U)
@app.route('/books/<int:id>',methods=['PUT'])
def edit_book_by_id(id):
    cursor = mydb.cursor()
    new_book = request.get_json()

    # No data sent
    if not new_book or not ('title' in new_book or 'writer' in new_book):
        return jsonify({'error': 'Invalid data.'}), 400

    # Catch the values and updates
    updates = []
    values = []
    if 'title' in new_book:
        updates.append("title = %s")
        values.append(new_book['title'])
    if 'writer' in new_book:
        updates.append("writer = %s")
        values.append(new_book['writer'])
        
    values.append(id)
    
    # Update de data sent
    sql = f"UPDATE books SET {', '.join(updates)} WHERE id = %s"
    cursor.execute(sql, tuple(values))
    mydb.commit()

    # If no one row changed returns an error
    if cursor.rowcount == 0:
        return jsonify({'error': 'Book not found!'}), 404

    return jsonify({'id': id, **new_book}), 200

# Delete (D)
@app.route('/books/<int:id>',methods=['DELETE'])
def delete_book(id): 

    # Delete data
    cursor = mydb.cursor()
    sql = f'DELETE FROM books WHERE id = %s;'
    cursor.execute(sql, (id,))
    mydb.commit()    


    # If no one row changed returns an error
    if cursor.rowcount == 0:
        return jsonify({'error': 'Book not found.'}), 404
    
    return jsonify({'message': f'Book with id: {id} deleted successfully.'}), 200


# Run app
app.run(port=CHANGE-ME,host='CHANGE-ME',debug=True)