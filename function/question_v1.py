def add_display(n):
    sum = 0
    for i in range(2,n):
        if n%i == 1:
            sum+=i 
            print(sum)
for i in range(2,10):
    out = add_display(i)
    print(i,out)
          





