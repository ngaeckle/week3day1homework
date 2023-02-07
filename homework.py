"""
Expected Output
Abraham Lincoln
Andrew P Garfield
Connor Milliken
Jordan Alexander Williams
None
None
"""
import re

with open("./regex.txt")as f:
    data = f.readlines()

pattern = re.compile("([A-Z][a-z]+) ([A-Z][a-z]*)* *([A-Z][a-z]+)")

for person in data:
    match = pattern.search(person)
    if match:
        if match.group(2):
            print(f"{match.group(1)} {match.group(2)} {match.group(3)}")
        else:
            print(f"{match.group(1)} {match.group(3)}")
    else:
        print("None")