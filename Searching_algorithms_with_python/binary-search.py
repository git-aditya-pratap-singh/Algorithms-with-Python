list=[]
found=0
start=0
size=int(input("Enter the size of the list : "))
for i in range(0,size):
    num=int(input("enter the numbers : "))
    list.append(num)
list.sort()
search=int(input("enter the searched elements : "))
end=size-1
while start<=end:
    mid=(start+end)//2
    if list[mid] == search:
        print("The number {} is found in given list ".format(search))
        found=1
        break
    elif list[mid] < search:
        start=mid+1
    else:
        end=mid-1
if found == 0:
    print("The numbers {} does not exist !".format(search))

     