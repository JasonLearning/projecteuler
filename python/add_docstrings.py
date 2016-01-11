#!/usr/bin/python

"""Add docstrings to Python modules"""

import os
from itertools import count
import requests
from bs4 import BeautifulSoup


def main():
    for num in count(1):
        filename = "problem{:03d}.py".format(num)

        if not os.path.exists(filename):
            break

        url = "https://projecteuler.net/problem="+str(num)
        r = requests.get(url)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        problem_number = soup.body.find("h3").text
        problem_title = soup.body.find("h2").text

        docstring = '"""{}: {}"""\n'.format(problem_number, problem_title)
        print(docstring[3:-4])

        with open(filename, "r+") as f:
            lines = f.readlines()

            if lines[2] != docstring:
                lines[2:2] = [docstring, "\n"]
                f.seek(0)
                f.writelines(lines)

if __name__ == "__main__":
    main()
