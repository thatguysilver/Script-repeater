#! /usr/bin/python3

'''
format: ./rept.py <command> <interval>
'''
import threading, os, sys, webbrowser

try:
    from selenium import webdriver

except ImportError:
    print("You need Selenium for browser languages")

def repeat():
    if sys.argv[1] == "cargo":
        to_run = sys.argv[1] + ' ' + sys.argv[2]
        seconds = sys.argv[3]
        threading.Timer(int(seconds), repeat).start()
        os.system(to_run)

    elif sys.argv[1][-2:] == 'js':
        print("{}".format(os.path.abspath(sys.argv[1])))
        to_run = os.path.abspath(sys.argv[1])
        browser = webdriver.Firefox()
        browser.get('{}'.format(to_run))

    else:
        to_run = sys.argv[1]
        seconds = sys.argv[2]
        threading.Timer(int(seconds), repeat).start()
        os.system("python3 " + format(to_run))

repeat()

