#! /usr/bin/python3

'''
format: ./rept.py <command> <interval>
'''
import threading, os, sys

def repeat():
    if sys.argv[1] == "cargo":
        to_run = sys.argv[1] + ' ' + sys.argv[2]
        seconds = sys.argv[3]
        threading.Timer(int(seconds), repeat).start()
        os.system(to_run)

    else:
        threading.Timer(int(seconds), repeat).start()
        os.system("python3 " + to_run)

repeat()

