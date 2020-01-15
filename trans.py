testfile = open("Email-Enron.txt", "r")
fromindex = []
toindex = []
for string in testfile:
    if string[-1] == '\n':
        string = string[:-1]
    line = string.split('	')
    first_part = line[0]
    second_part = line[1]
    if second_part > first_part:
        fromindex.append(first_part)
        toindex.append(second_part)
testfile.close()  

f = open('Graph-Email','w')
f.write('t 1 36692\n')
for i in range(36692):
    f.write('v ' + str(i) + ' 0\n')
for i in range(len(fromindex)):
    f.write('e ' + str(fromindex[i]) + ' ' + str(toindex[i]) + ' ' +  '0\n')
f.close()


