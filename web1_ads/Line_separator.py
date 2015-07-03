lines = open('line.txt', 'r').readlines()

lines_set = set(lines)

out  = open('workfile.txt', 'w')

for line in lines_set:
    out.write(line)
