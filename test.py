i = 0
while i < 10:
    print(i)
    if i % 2 == 0:
        print('even')
        i+=1
        #continue
    if i %3 == 0:
        print('three')
        i+=1
        continue
    i+=1