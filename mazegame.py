array = []

with open('maze1.txt', 'r') as f:
        for line in f.readlines():
            array.append(line.split(' '))
print(array)