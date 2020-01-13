writeto = open("Q_Email-Enron.txt", "w")
writeto.write("t # 0\n")

for i in range(36692):
    writeto.write("v "+ str(i) + " 0\n")

file = open("Email-Enron.txt")
count = 0
for line in file:
    divide = line.split("	")
    start = divide[0]
    end = divide[1]
    if end[-1] == '\n':
        end = end[:-1]
    writeto.write("e "+ str(start) + " " + str(end) + " 0\n")

file.close()
writeto.close()
