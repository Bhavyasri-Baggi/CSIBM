import sqlite3
from pynput import keyboard


def read_keystrokes():
    conn = sqlite3.connect("keystrokes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM keystrokes")
    rows = cursor.fetchall()
    conn.close()

    return rows

if __name__ == "__main__":
    rows = read_keystrokes()
    print("ID\tKeystroke")
    print("--\t---------")
    for row in rows:
        print(f"{row[0]}\t{row[1]}")

    def stop_script():
        print("\nStopping the script.")

    try:
        keyboard.Listener(on_press=stop_script).join()
    except KeyboardInterrupt:
        print("\nStopping the script.")