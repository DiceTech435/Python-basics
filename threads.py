import threading 

class messenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())

s = messenger(name="Send message")
r = messenger(name="Recieve message")

s.start()
r.start()