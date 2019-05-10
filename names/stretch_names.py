import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")
f.close()

# the other (much less cool) way to do this would be to make a BST in the form of a list, which would adhere more closely to
# what the question asked


# technically speaking this one works too and duplicates is still stored as a list
duplicates = [x for x in set(names_1) & set(names_2)]

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
