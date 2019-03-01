import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


duplicates = []
# takes 9-11 seconds
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# first attempt, takes 2-3 secones
# for name in names_1:
#     if name in names_2:
#         duplicates.append(name)

# second attempt, takes less than a millisecond...crazy!

# https://stackoverflow.com/questions/1388818/how-can-i-compare-two-lists-in-python-and-return-matches

a = set(names_1)
b = set(names_2)

duplicates.append(str(a & b))


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
