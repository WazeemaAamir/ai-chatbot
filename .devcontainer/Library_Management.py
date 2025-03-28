import streamlit as st
import sqlite3

# Database setup
def init_db():
    conn = sqlite3.connect("library.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, genre TEXT, copies INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS issued_books (id INTEGER PRIMARY KEY, book_id INTEGER, user TEXT, FOREIGN KEY(book_id) REFERENCES books(id))''')
    conn.commit()
    conn.close()

# Function to add a book
def add_book(title, author, genre, copies):
    conn = sqlite3.connect("library.db")
    c = conn.cursor()
    c.execute("INSERT INTO books (title, author, genre, copies) VALUES (?, ?, ?, ?)", (title, author, genre, copies))
    conn.commit()
    conn.close()

# Function to get all books
def get_books():
    conn = sqlite3.connect("library.db")
    c = conn.cursor()
    c.execute("SELECT * FROM books")
    books = c.fetchall()
    conn.close()
    return books

# Function to issue a book
def issue_book(book_id, user):
    conn = sqlite3.connect("library.db")
    c = conn.cursor()
    c.execute("SELECT copies FROM books WHERE id = ?", (book_id,))
    copies = c.fetchone()[0]
    if copies > 0:
        c.execute("INSERT INTO issued_books (book_id, user) VALUES (?, ?)", (book_id, user))
        c.execute("UPDATE books SET copies = copies - 1 WHERE id = ?", (book_id,))
        conn.commit()
    conn.close()

# Function to return a book
def return_book(book_id):
    conn = sqlite3.connect("library.db")
    c = conn.cursor()
    c.execute("DELETE FROM issued_books WHERE book_id = ?", (book_id,))
    c.execute("UPDATE books SET copies = copies + 1 WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()

# Streamlit UI
st.title("📚 Library Management System")
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Add Book", "View Books", "Issue Book", "Return Book"])

init_db()

if page == "Add Book":
    st.subheader("Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    genre = st.text_input("Genre")
    copies = st.number_input("Copies Available", min_value=1, step=1)
    if st.button("Add Book"):
        add_book(title, author, genre, copies)
        st.success("Book added successfully!")

elif page == "View Books":
    st.subheader("Available Books")
    books = get_books()
    for book in books:
        st.text(f"{book[0]}. {book[1]} by {book[2]} (Genre: {book[3]}, Copies: {book[4]})")

elif page == "Issue Book":
    st.subheader("Issue a Book")
    books = get_books()
    book_options = {f"{book[1]} by {book[2]}": book[0] for book in books}
    book_choice = st.selectbox("Select a book", list(book_options.keys()))
    user = st.text_input("User Name")
    if st.button("Issue Book"):
        issue_book(book_options[book_choice], user)
        st.success(f"{book_choice} issued to {user}!")

elif page == "Return Book":
    st.subheader("Return a Book")
    books = get_books()
    book_options = {f"{book[1]} by {book[2]}": book[0] for book in books}
    book_choice = st.selectbox("Select a book to return", list(book_options.keys()))
    if st.button("Return Book"):
        return_book(book_options[book_choice])
        st.success(f"{book_choice} returned successfully!")
