import csv

data = []

with open('lab2.csv') as csvf:
    reader = csv.reader(csvf)
    for row in reader:
        data.append(row)

S = ['phi'] * (len(data[0])-1)
G = ['?'] * (len(data[0])-1)
print('S 0: ', S)
print('G 0: ', G)
cnt = 0

all_possible_values = dict()
for i in range(len(data[0])-1):
    if i not in all_possible_values.keys():
        all_possible_values[i] = set()
    for j in range(len(data)):
        all_possible_values[i].add(data[j][i])

for x in data:
    if x[-1] == 'Y':
        for i in range(len(x)-1):
            if S[i] == 'phi' or x[i] == S[i]:
                S[i] = x[i]
            else:

                search_str = '<' + ' ? '*i + S[i] + ' ? '*(len(S)-i-1) + '>'
                if search_str in G:

                    G.remove(search_str)
                S[i] = '?'
    elif x[-1] == 'N':
        if '?' in G:
            G = [g for g in G if g != '?']

            for i in range(len(x)-1):
                if S[i] != x[i] and S[i] != '?':
                    for possibleVals in all_possible_values[i]:

                        if possibleVals != x[i]:
                            new = '<' + ' ? '*i + possibleVals + ' ? ' * \
                                (len(S)-i-1) + \
                                '>'
                            if new not in G:
                                G.append(new)
        for i in range(len(x)-1):
            if S[i] != x[i] and S[i] != '?':
                search_str = '<' + ' ? '*i + x[i] + ' ? '*(len(S)-i-1) + '>'
                if search_str in G:
                    G.remove(search_str)
    cnt += 1
    print('S', cnt, ': ', S, '   ',)
    print('G', cnt, ': ', G)