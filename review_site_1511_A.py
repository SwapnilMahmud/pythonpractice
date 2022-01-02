for i in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    count_1=0
    count_2=0
    count_3=0
    for j in li:
        if j==1:
            count_1+=1
        elif j==2:
            count_2+=1
        elif j==3:
            count_3+=1
    print(count_1+count_3)
