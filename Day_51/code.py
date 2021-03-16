file = []
for i in range(1000, 5001):
    if (i%9 == 0 and not (i%7 == 0)):
        file.append(str(i))
print(",".join(file))