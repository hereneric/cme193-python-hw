import operator

content = []
with open('shakespeare.txt', 'r') as f:
    for line in f:
        content.append(line.strip('\r\n '))
f.close()
dic = {}
for line in content:
    words = line.split()
    for word in words:
        dic[word] = dic.get(word, 0) + 1
sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))
for tup in sorted_dic[-20:]:
    print tup[0]

print "How many unique words? " + str(len(dic))
count = 0
for tup in sorted_dic:
    if tup[1] >= 5:
        count += 1
print "How many words are used at least 5 times? " + str(count)
with open('top200common.txt', 'w') as f:
    for tup in sorted_dic[-200:]:
        f.write(str(tup[0]) + ' ' + str(tup[1]) + '\n')
f.close()
