data = []
found = 0
start = 0
size = int(input("Enter the size of the list : "))
for i in range(0, size):
    num = int(input("enter the numbers : "))
    data.append(num)
data.sort()
search = int(input("enter the searched elements : "))

# Apply binary searching algorithms ----------

end = size-1
while start <= end:
    mid = (start+end)//2
    if data[mid] == search:
        print("The number {} is found in given list ".format(search))
        found = 1
        break
    elif data[mid] < search:
        start = mid+1
    else:
        end = mid-1
if found == 0:
    print("The numbers {} does not exist !".format(search))

# Time Complexity----
'''
Best case => O(1)
Wrost Case => ...n (length of array)
              ...n/2 (half of n)
              ...n/4 (half of n/2)
              ...n/8 (half of n/4)
              ...1 (find value)

=> n/2^k=1
=> 2^k = n
=> take both side log ---
=> (log) 2^k =(log) n 
=> k log2 = log(n) {---> log(2) = 1}
=> k = log(n)
=> O(log n) 
'''

# Space Complexity---
'''
N => (length of array)
+1 => (for mid)
+1 => (for start)
+1 => (for end)
+1 => (for key)
=> S(x) = N+4
=> O(n)
'''

# ---------------- Written By : - Aditya Pratap Singh ------------------
