import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="armaan@1234",
    database="nexus_db"
)

cursor = conn.cursor()

# ---------------- USER FUNCTIONS ----------------

def add_user(username, password):
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (username, password)
    )
    conn.commit()

def login_user(username, password):
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())  # 👈 DEBUG

    cursor.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s",
        (username, password)
    )
    return cursor.fetchone()
# ---------------- CHAT FUNCTIONS ----------------

def save_chat(username, message, response):
    cursor.execute(
        "INSERT INTO chats (username, message, response) VALUES (%s, %s, %s)",
        (username, message, response)
    )
    conn.commit()

def get_chats(username):
    cursor.execute(
        "SELECT message, response FROM chats WHERE username=%s",
        (username,)
    )
    return cursor.fetchall()