data = []
count = 0
while True:
    num = int(input(f"Enter the Number at {count} : "))
    if num == -1:
        break
    data.append(num)
    count += 1

# Display before Sorting algorithms----
print(f"without Sorting Array -------> {data}")

# Apply Bubble sorting algorithms ----------
'''
if length of Array is --> 5
if i = 0, then j = 0,1,2,3.
if i = 1, then j = 0,1,2.
if i = 2, then j = 0,1.
if i = 3, then j = 0.
'''

size = len(data)
for i in range(size-1):
    for j in range(size-1-i):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]

# Display after Sorting algorithms----
print(f"Bubble Sort -------> {data}")

# Time Complexity----
'''
Best Case => O(n)
Wrost Case => ------
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

