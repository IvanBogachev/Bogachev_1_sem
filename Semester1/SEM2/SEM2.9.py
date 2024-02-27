m=0
punctuation_marks = ['!', '?', '.']
with open('input.txt', 'r') as f1, open('output.txt', 'w') as f2:
    lines=f1.readlines()
    line = lines[0]
    line = line.split()
    for i in range(len(line)):
        if line[i].find('.')>-1 or line[i].find('?')>-1 or  line[i].find('!')>-1 :
            m+=1
        else:
            m+=0

    f2.writelines(str(m))
print(m)