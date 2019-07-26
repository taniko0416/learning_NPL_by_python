import json
import sqlite3

# SQLiteの便利関数を作成
conn = None

def connect():
    # global：グローバル変数にする
    global conn
    conn = sqlite3.connect('./sample.db')

def close():
    conn.close()

def create_table():
    
    # executeはSQLを実行するためのメソッド
    conn.execute('DROP TABLE IF EXISTS docs')
    conn.execute('''CREATE TABLE docs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT,
        meta_info BLOB,
        sentence BLOB,
        chunk BLOB,
        token BLOB
    )''' )

# 一度に複数のSQL文を実行したいときは，タプルのリストを作成した上で
# executemanyメソッドを実行する
# commitで実行
def load(values):
    conn.executemany(
        'INSERT INTO docs (content,meta_info) VALUES (?,?)',values
)
    conn.commit()

def get(doc_id, fl):
    row_ls = conn.execute(
        'SELECT {} FROM docs WHERE id = ?'.format(','.join(fl)),
        (doc_id,)).fetchone()
    row_dict = {}
    for key,value in zip(fl,row_ls):
        row_dict[key] = value
    return row_dict

def get_all_ids(limit, offset=0):
    return [record[0] for record in
        conn.execute(
            'SELECT id FROM docs LIMIT ? OFFSET ?',
            (limit,offset))]
