#!/usr/bin/env python3

import os


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

def delete_empty_folders():
    notify('Script', 'Script is currently running')
    path = '/enter/path/here'
    os.chdir(path)
    directory = os.walk(path)
    content = next(directory)
    for dir in content[1]:
        if not os.listdir(dir):
            os.rmdir(dir)
