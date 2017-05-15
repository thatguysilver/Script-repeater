#! usr/bin/python3

import threading, os

def repeat():
    threading.Timer(1.0, repeat).start()
    os.system('python3 test.py')
repeat()

