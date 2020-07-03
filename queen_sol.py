import itertools as it
def is_solution(prem):
    for (i1,i2) in it.permutations(range(len(prem)),2):
        if abs(i1-i2) is abs(prem[i1]-prem[i2]):
            return False

    return True

def bc_tc(prem,n):
    if len(prem) is n:
        print(prem)
        exit()
    for k in range(n):
        if k not in prem:
            prem.append(k)
            if is_solution(prem):
                bc_tc(prem,n)
            prem.pop()


inp = input('Enter how many queen you have to set:')
bc_tc(prem=[],n=int(inp))
