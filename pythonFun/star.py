n=int(input("enter number /n"))
for i in range(1,n+1):
    for j in range(1,i+1):

        if i==j or j==1:
            print(" ",end=" ")
        else: 
            print(" ",end=" ")

    print()
for i in range(n-1,0,1):
  for j in range(1,i+1):
    if j==1 or i==j:
        print("*",end="")

    print()