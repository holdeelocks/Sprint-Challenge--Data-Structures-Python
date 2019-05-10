import time

start_time = time.time()

# this could be done with a BST but I found a more optimal solution before I even thought of using a BST, so I won't bother
# including BST code in this, just pretend i pasted my BST code in here and made the slower solution that way if you like

f = open('names_1.txt', 'r')
# optimal runtime solution here
names_1 = set(name for name in f.read().split('\n'))
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")
f.close()

duplicates = []

for name in names_2:
    if name in names_1:
        duplicates.append(name)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
