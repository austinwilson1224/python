campNumbers = {}
campNumbers[(1,3,5)] = 2
campNumbers[(3,2,1)] = 6
campNumbers[(1,3)] = 10

sum = 0

for k in campNumbers:
    sum += campNumbers[k]


sum

len(campNumbers)
print(len(campNumbers) + sum)