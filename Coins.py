import itertools

sample = list(itertools.product(["H", "T"], repeat=2))

A = [s for s in sample if s[0] == "H"]
B = [s for s in sample if "H" in s]

A_and_B = [s for s in A if s in B]

print(len(A_and_B)/len(B))

sample = list(itertools.product([1, 2, 3, 4, 5, 6], repeat=2))
B = [s for s in sample if 6 in s]
A = [s for s in sample if s[0] == 6 and s[1] == 6]

A_and_B = [s for s in A if s in B]
print(len(A_and_B)/len(B))