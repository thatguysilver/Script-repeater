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

    elif sys.argv[1][-4:] == 'html':

        print("Opening " + os.path.abspath(sys.argv[1]) + " in a new window.")
        
        seconds = sys.argv[2]
        browser = webdriver.Firefox()
        browser.get('file://' + os.path.abspath(sys.argv[1]))
        threading.Timer(int(seconds), repeat).start()
        browser.navigate().refresh()



    else:
        to_run = sys.argv[1]
        seconds = sys.argv[2]
        threading.Timer(int(seconds), repeat).start()
        os.system("python3 " + to_run)

repeat()

