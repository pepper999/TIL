T = int(input())
 
for i in range(T):
    final = 1
    a = list()
    for j in range(9):
        a.append(list(map(int, input().split())))
        if len(list(set(a[j]))) != 9:
               final = 0
        else:
               pass
    for j in range(9):
        col = list()
        for k in range(9):
            col.append(a[k][j])
        if len(set(col)) != 9:
            final = 0
        else:
               pass
     
    box = list()
    for j in range(9):
        for k in range(3):
            for l in range(3):
                box.append(list(a[k*3][l*3:(l*3)+3] + a[(k*3)+1][l*3:(l*3)+3] + a[(k*3)+2][l*3:(l*3)+3]))
        if len(set(box[j])) != 9:
            final = 0
        else:
              pass
    print(f'#{i+1}', final)