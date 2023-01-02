#!/usr/bin/env python3
from sys import argv
from os import mkdir
from datetime import date

title_fmt = lambda s: (s[0].upper() + s[1:]).replace("_", " ")

for name in argv[1:]:
    try:
        mkdir(name)
        with open(name + "/index.md", "w+") as file:
            file.write("---\n")
            file.write("title: \"{}\"\n".format(title_fmt(name)))
            file.write("date: {}\n".format(date.today().strftime("%Y-%m-%d")))
            file.write("description: \"\"\n")
            file.write("tags: \n")
            file.write("---\n")
        print("Created new page: " + name)
    except IOError as e:
        print(e)
print("\nExiting...")
