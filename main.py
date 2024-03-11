import sqlite3

# con = sqlite3.connect('db.sqlite')
# cur = con.cursor()

# cur.execute('''
# DELETE FROM users5;
# ''')
# con.commit()
# con.close()


user = {
    'user_id': 1215,
    'subject': 'js',
    'level': 'beginner',
    'task': '',
    'answer': ''
}
print(f'user {user}')


# query = '''
#     INSERT INTO users5(user_id, subject, level)
#     VALUES (1111,"js", "adw");
# '''
# cur.execute(query)
# con.commit()
# con.close()

# def get_data():
#     con = sqlite3.connect('db.sqlite')
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
# #
#     current_user = {
#         'user_id': '',
#         'subject': '',
#         'level': '',
#
#     }
#     query = cur.execute('''
#         SELECT user_id, subject, level
#         FROM users5
#         LIMIT 1
#         ''')
#
#     for item in query:
#         print(type(item['user_id']))
#         # print(item['subject'])
#         # print(item['level'])
#         # user['user_id'] = item['user_id']
#         # user['subject'] = item['subject']
#         # user['level'] = item['level']
#         print('------------------')
#         current_user['user_id'] = item['user_id'],
#         print(item['user_id'])
#         current_user['subject'] = item['subject'],
#         current_user['level'] = item['level'],
#
#     con.close()
#     print(current_user)
#     return current_user
#
# #
# cur_user = get_data()
# print(f'by func {cur_user["user_id"]}')


def insert_data(user_id=None, subject=None, level=None, task=None, answer=None):
    try:
        con = sqlite3.connect('db.sqlite')
        cur = con.cursor()
        cur.execute(f'INSERT INTO users6(user_id, subject, level, task, answer)'
                    f'VALUES (?, ?, ?, ?, ?);',
                    (user_id, subject, level, task, answer))
        print('data is written to the database')
        con.commit()
    except sqlite3.Error as error:
        print(f'Error database:', error)
    finally:
        con.close()



tsk = 'how many variable....'
ans = 'Very many....'

insert_data(user['user_id'], user['subject'], user['level'], tsk, ans)

# query = cur.execute('SELECT * FROM video_products')
# for res in query:
#     print(res)
# print(query)

# con.commit()

# def create_users_table():
#     con = sqlite3.connect('db.sqlite')
#     cur = con.cursor()
#     cur.execute('''
#         CREATE TABLE IF NOT EXISTS users6(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user_id INTEGER,
#         subject TEXT,
#         level TEXT,
#         task TEXT,
#         answer TEXT
#     );
#     ''')

# create_users_table()
