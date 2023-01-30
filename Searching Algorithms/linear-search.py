data = []
found = 0
size = int(input("Enter The size of the list : "))
for i in range(0, size):
    num = int(input("Enter the numbers : "))
    data.append(num)
search = int(input("Enter the searched element in the given list : "))
for j in range(0, size):
    if list[j] == search:
        print("The element {} is present at the position {}".format(search, j))
        found = 1
        break
    
if found == 0:
    print("The Element {} is does not exist !".format(search))

# Time Complexity----
'''
Best case => O(1)
Wrost Case => O(n) ---> depend on length of array
'''
# Space Complexity---
'''
N => (length of array)
=> O(n)
'''

# ---------------- Written By : - Aditya Pratap Singh ------------------
