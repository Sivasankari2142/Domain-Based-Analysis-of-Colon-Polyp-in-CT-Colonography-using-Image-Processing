n=int(input())
for i in range(0,n):
  decimal=list(map(int,input().strip().split(" ")))
lst=[]
difference=[]
for i in range(0,n):
  c=bin(i)
  lst.append(c)
lst1=[]
for i in range(0,n):
  d=bin(c)
  lst1.append(d)
zip_object=zip(lst,lst1)
for lst_i,lst1_i in zip_object:
    difference.append(lst_i-lst1_i)
BinaryToDecimal(difference)
def BinaryToDecimal(binary): 
    decimal = 0 
    for digit in binary: 
        decimal = decimal*2 + int(digit) 
    difference.append(decimal)
print(decimal)
