# file = open ("challengeone.txt","r")

total_score = 0
counter = 0
max_score = 0
min_score = 100
max = 0
max_name = ""
min_name = ""
# create the dictionary 
dictionary = {}
with open("challengeonenames.txt") as file:
    for line in file:
        (name, score) = line.split()
        score = int(score)
        dictionary[name] = score

    
for key in dictionary:
    score = dictionary[key]
    total_score = total_score + score
    counter = counter + 1
    average_score = total_score/counter

for name in dictionary:
    score = dictionary[name]
    
    if score > max_score:
        max_name = name
        max_score = score

for name in dictionary:
    score = dictionary[name]
    if score < min_score:
        min_score = score 
        min_name = name
print (max_name)
print( f"max_score: {max_score}")
print(f"average score: {average_score}")
print (f"lowest name: {min_name}")






# for line in file.readlines():
#     num = int(line.split(",")[0])
#     if (max < num):
#         max = num 
# print(max)

 