file = open("test.txt", "r")
n = dict()
for i in file:
    i = i.strip()
    i = i.lower()
    words = i.split(" ")
    for word in words:
        if word in n:
            n[word] = n[word] + 1
        else:
            n[word] = 1

for k in list(n.keys()):
    print(k, " ", n[k])