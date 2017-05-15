#! /usr/bin/python3

'''
format: ./rept.py <command> <interval>
'''
import threading, os, sys

def repeat():
    to_run = sys.argv[1]                    #command
    seconds = sys.argv[2]                   #interval
   
    threading.Timer(int(seconds), repeat).start()
    os.system("python3 " + to_run)

repeat()

