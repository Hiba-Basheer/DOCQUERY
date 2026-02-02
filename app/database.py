import sqlite3
from datetime import datetime

db_name = 'content.db'

# creating table for saving the contents
def create_tab():
    # connecting to sqlite3
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    # creating table
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS contents (
                       doc_id TEXT PRIMARY KEY,
                       file_name TEXT,
                       text TEXT,
                       metadata TEXT,
                       created_at TEXT
        )
    ''')
    # saving all changes
    con.commit()
    # closing the connection to the db
    con.close()
    
# saving contents
def save_contents(doc_id, file_name, text, metadata):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    # inserting values into the table
    cursor.execute(
        'INSERT INTO contents (doc_id, file_name, text, metadata, created_at) VALUES (?, ?, ?, ?, ?)',
        (doc_id, file_name, text, str(metadata), datetime.now().isoformat())
    )
    con.commit()
    con.close()
    print(f'Document {doc_id} saved succesfully')
    
# retrieving texts
def get_document_text(doc_id):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    cursor.execute('SELECT text FROM contents WHERE doc_id = ?', (doc_id))
    # fetching one row
    row = cursor.fetchone()
    con.close()
    # fetching the text from the row
    return row[0] if row else ''
    