import itertools as it
def is_solution(prem):
    for (i1,i2) in it.combinations(range(len(prem)),2):
        if abs(i1-i2)==abs(prem[i1]-prem[i2]):
            #print("Is not a solution.")
            return False

    #print('its a solution.')
    return True

def bc_tc(prem,n):
    if len(prem) is n:
        print(prem)
        #exit()
        return
    for k in range(n):
        if k not in prem:
            prem.append(k)
            if is_solution(prem):
                bc_tc(prem,n)
            prem.pop()

bc_tc(prem=[],n=5)
