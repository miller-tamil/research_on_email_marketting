with open('line.txt') as result:
        uniqlines = set(result.readlines())
        with open('line2.txt', 'w') as rmdup:
            rmdup.writelines(set(uniqlines))