import random

wordlist = []

with open("wiki.txt",'r') as file:
    data = file.readlines()
for line in data:

    #1.print(data)

    #2.print(line)
    words = line.split()
    
    for item in words:
        if len(item) > 5:
         wordlist.append(item.capitalize())


word = random.choice(wordlist)
schar=random.choice('special_char')
num = str(random.randint(10, 99))

passw = word + schar + num
print(passw)
        
    
    