'''import pync
import os

pync.notify('Hello World')
pync.notify('Hello World', title='Python')
pync.notify('Hello World', group=os.getpid())
pync.notify('Hello World', activate='com.apple.Safari')
pync.notify('Hello World', open='http://github.com/')
pync.notify('Hello World', execute='say "OMG"')

pync.remove_notifications(os.getpid())

pync.list_notifications(os.getpid())
'''
import os

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

notify("Title", "Heres an alert")
