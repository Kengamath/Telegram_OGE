import sqlite3 as sq

db = None
cur = None

async def db_start():
    global db, cur

    db = sq.connect('sights.db')
    cur = db.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS photos (
        id INTEGER PRIMARY KEY,
        topic TEXT NOT NULL,
        photo_path TEXT NOT NULL
    )
    ''')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL UNIQUE,
        reminder_time TEXT
    )
    ''')
    db.commit()

async def add_photo(topic, photo_path):
    cur.execute("INSERT INTO photos(topic, photo_path) VALUES (?,?)", (topic, photo_path))
    db.commit()

async def get_photo(topic):
    cur.execute("SELECT photo_path FROM photos WHERE topic=?", (topic,))
    photo_path = cur.fetchone()
    return photo_path

async def add_reminder(user_id, reminder_time):
    cur.execute("INSERT INTO users (user_id, reminder_time) VALUES (?, ?)", (user_id, reminder_time))
    db.commit()

async def get_users_for_reminder(current_time):
    cur.execute("SELECT user_id FROM users WHERE reminder_time = ?", (current_time,))
    users = cur.fetchall()
    return users

async def user_already_set_reminder(user_id):
    cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = cur.fetchone()
    return user is not None