#Fibonacci Generator

iter = int(input("Enter Number of iteration: "))
Num1 = 0
Num2 = 1
OutPut = Num2

count = 1
while count <= iter:
    print(OutPut, end=" ")
    Num1, Num2 = Num2, OutPut
    OutPut = Num1 + Num2
    count += 1
