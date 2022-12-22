from sys import argv
from os import mkdir
from datetime import date

firstLetterUpper = lambda s: s[0].upper() + s[1:]

for name in argv[1:]:
    try:
        mkdir(name)
        with open(name + "/index.md", "w+") as file:
            file.write("---\n")
            file.write("title: \"{}\"\n".format(firstLetterUpper(name)))
            file.write("date: {}\n".format(date.today().strftime("%Y-%m-%d")))
            file.write("description: \"\"\n")
            file.write("tags: \n")
            file.write("---\n")
    except IOError as e:
        print(e)
