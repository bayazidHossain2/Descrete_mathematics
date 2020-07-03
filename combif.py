arr={1,2,3,4};
import itertools as it
print("Start combination.")
ii=1
for (i1,i2,i3) in it.combinations(range(6),3):
    print(ii,i1,i2,i3)
    ii+=1
print("Combination finished.")
