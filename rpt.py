#! /usr/bin/python3

import threading, os, sys

def repeat():
    to_run= sys.argv[1]
    
    threading.Timer(1.0, repeat).start()
    os.system("python3 " + to_run)

repeat()

