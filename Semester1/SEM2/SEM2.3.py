st = input()
mirror_letters = ['E', '3', 'S', '5', 'Z', '2', 'J', 'L']
symmetric_letters = ['A', 'M', 'H', 'I', 'V', 'W', 'O', 'T', 'X', 'Y', 'U', '1', '8']
L = len(st)
num_steps = L // 2 + 1
palin = True
mirror = True
for i in range(num_steps):
    if st[i] not in symmetric_letters and st[i] not in mirror_letters :
        mirror = False
    elif st[i] in symmetric_letters:
        if st[i] != st[-(i+1)]:
            mirror = False
    else:
        if st[i] == 'E' :
            if st[-(i+1)] != '3':
                mirror = False
        if st[i] == 'L' :
            if st[-(i+1)] != 'J':
                mirror = False
        if st[i] == 'Z' :
            if st[-(i+1)] != '5':
                mirror = False
        if st[i] == 'S' :
            if st[-(i+1)] != '2':
                mirror = False
for i in range(num_steps):
    if st[i] != st[-(i+1)]:
        palin = False
        break
if palin == False and mirror == False:
    print(st,'is not a palindrome.')
if palin == True and mirror == False:
    print(st, 'is a regular palindrome.')
if palin == False and mirror == True:
    print(st,'is a mirrored string.')
if palin == True and mirror == True:
    print(st, 'is a mirrored palindrome')












