#python program to print numbers in triangular loop
rows=int(input ("enter the number of rows:"))
for i in range(rows,0,-1):
    print("\n")
    for j in range(rows-i+1):
        print(i,"",end="")
 
    
    
