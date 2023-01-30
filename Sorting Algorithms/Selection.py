data = []
count = 0
while True:
    num = int(input(f"Enter the Number at {count} : "))
    if num == -1:
        break
    data.append(num)
    count += 1

# Display before Sorting algorithms----
print(data)

# Apply Selection sorting algorithms ----------

''' if length of data(list) = 5, 
if i = 0 then j = 1,2,3,4. 
if i = 1 then j = 2,3,4. 
if i = 2 then j= 3,4.
if i = 3 then j= 4.'''

length = len(data)
for i in range(length-1):
    for j in range(i+1, length):
        if data[i] > data[j]:
            data[i], data[j] = data[j], data[i]

# Display after Sorting algorithms----
print(data)

# Time Complexity----
'''
t(x) = 1+2+3+4+........N
=> N*(N+1)/2
t(x) = 1+2+3+4+........N-1
=> (N-1)*(N-1+1)/2
=> N^2-N/2
=> O(n^2)
'''

# Space Complexity---
'''
N => (List of data)
+1 => (Length of list)
+1 => (for i)
+1 => (for j)
=> S(x) = N+3
=> O(n)
'''

# ---------------- Written By : - Aditya Pratap Singh ------------------
