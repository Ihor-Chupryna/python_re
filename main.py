import sqlite3

# con = sqlite3.connect('db.sqlite')
# cur = con.cursor()

def delete_data(id):
    try:
        con = sqlite3.connect('db.sqlite')
        cur = con.cursor()
        cur.execute(f'DELETE FROM users2 WHERE user_id = ?', (id,))
        con.commit()
        print('----')
    except sqlite3.Error as error:
        print('error from database:', error)
    finally:
         con.close()

delete_data(1111)
#
# user = {
#     'user_id': 1215,
#     'subject': 'js',
#     'level': 'beginner',
#     'task': '',
#     'answer': ''
# }
# print(f'user {user}')


# query = '''
#     INSERT INTO users5(user_id, subject, level)
#     VALUES (1111,"js", "adw");
# '''
# cur.execute(query)
# con.commit()
# con.close()

# def get_data():
#     user = {}
#     try:
#         con = sqlite3.connect('db.sqlite')
#         cur = con.cursor()
#         query = cur.execute('''
#             SELECT user_id, subject, level
#             FROM users5
#             LIMIT 1
#             ''')
#
#         res = query.fetchall()
#         user['user_id'] = res[0][0]
#         user['user_id'] = res[0][1]
#         user['subject'] = res[0][2]
#         user['level'] = res[0][3]
#         print('gеt data from database')
#     except sqlite3.Error as error:
#         print('error from db:', error)
#     finally:
#         con.close()
#         return user
# #
# # get_data()
# cur_user = get_data()

# print(f'return func {cur_user["user_id"]}, {cur_user["subject"]}, {cur_user["level"]}')


# def insert_data(user_id=None, name=None, subject=None, level=None, task=None, answer=None):
#     try:
#         con = sqlite3.connect('db.sqlite')
#         cur = con.cursor()
#         cur.execute(f'INSERT INTO users6(user_id, name, subject, level, task, answer)'
#                     f'VALUES (?, ?, ?, ?, ?, ?);',
#                     (user_id, name, subject, level, task, answer))
#         print('data is written to the database')
#         con.commit()
#     except sqlite3.Error as error:
#         print(f'Error database:', error)
#     finally:
#         con.close()
#
#
#
# tsk = 'how many variable....'
# ans = 'Very many....'
#
# insert_data(cur_user["user_id"], cur_user["subject"], cur_user["level"], tsk, ans)

# query = cur.execute('SELECT * FROM video_products')
# for res in query:
#     print(res)
# print(query)

# con.commit()

# def create_users_table():
#     con = sqlite3.connect('db.sqlite')
#     cur = con.cursor()
#     cur.execute('''
#         CREATE TABLE IF NOT EXISTS users_fin(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user_id INTEGER,
#         user INTEGER
#         subject TEXT,
#         level TEXT,
#         task TEXT,
#         answer TEXT
#     );
#     ''')

# create_users_table()
