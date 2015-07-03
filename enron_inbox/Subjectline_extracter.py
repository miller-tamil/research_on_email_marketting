from glob import glob
import fileinput
import os

with open('output.txt', 'w') as out:
    files = (os.path.join(p, f) for p, ds, fs in os.walk(os.curdir) for f in fs)
    for line in fileinput.input(files):
        if 'Subject:' in line:
            out.write(line)
