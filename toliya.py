from random import shuffle
spisok = []

trics = input('gcb? ')

while trics != 'horosh':
    if trics in spisok:
        print('ты егого?')
    else:
        spisok.append(trics)


spisok_bldender = []
nums = int(input())
for i in range(nums):
    shuffle(spisok)
    spisok_bldender.append(spisok[0])
    spisok.remove(spisok[0])

for i in range(nums):
    print(spisok_bldender[i])