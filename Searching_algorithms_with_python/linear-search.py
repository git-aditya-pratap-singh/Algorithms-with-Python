list=[]
found=0
size=int(input("Enter The size of the list : "))
for i in range(0,size):
    num=int(input("Enter the numbers : "))
    list.append(num)
search=int(input("Enter the searched element in the given list : "))
for j in range(0,size):
    if list[j] == search :
        print("The element {} is present at the positin {}".format(search,j))
        found=1
        break
    
if found == 0:
    print("The Element {} is does not exist !".format(search))   
