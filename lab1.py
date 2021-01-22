import csv

with open('data.csv') as csvFile:
    data = [line[:-1] for line in csv.reader(csvFile) if (line[-1] == "Y")]

S = ['o'] * len(data[0])
print(S)

for example in data:
    i = 0
    for feature in example:
        if (S[i] == feature or S[i] == "o"):
            S[i] = example
        else:
            S[i] = '?'
        i += 1
    print(S)
    