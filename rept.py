#! /usr/bin/python3

'''
format: ./rept.py <command> <interval>
'''
import threading, os, sys, webbrowser

try:
    from selenium import webdriver
except ImportError:
    print("Sorry! You'll have to install Selenium to use this.")
    sys.exit()

def repeat():
    '''Reads the filetype and runs it. Currently supports .rs (using Cargo only), .py and .html.'''

    if sys.argv[1] == "cargo":
        to_run = sys.argv[1] + ' ' + sys.argv[2]
        seconds = sys.argv[3]
        threading.Timer(int(seconds), repeat).start()
        os.system(to_run)

    elif sys.argv[1][-4:] == 'html':

        print("Opening " + os.path.abspath(sys.argv[1]) + " in a new window.")
        
        browser = webdriver.Firefox()
        browser.get('file://' + os.path.abspath(sys.argv[1]))
        
        while True:
            browser.refresh()

    else:
        to_run = sys.argv[1]
        seconds = sys.argv[2]
        threading.Timer(int(seconds), repeat).start()
        print('output')
        os.system("python3 " + to_run)
        print('end output')

repeat()

