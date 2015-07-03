with open ('text.txt', 'r') as f:
    names = sorted (name.rstrip ('\n') for name in f)

print (names)
