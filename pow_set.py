arr={3,2,5,6}
import itertools as it
r=3
for r in range(4):
    for aa in it.combinations(range(4),r+1):
        for v : aa:
            print(arr[v])
print("Complete set.")
