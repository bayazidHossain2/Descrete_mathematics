def g_p(prem,n):
    print("Function start again.")
    if len(prem)==n:
        print(prem)
        return
    for k in range(n):
        print("loop value ",k)
        if k not in prem:
            prem.append(k)
            print("append ",k)
            g_p(prem,n)
            print("Before pop ",prem)
            prem.pop()
            print("After pop ",prem)
    print("function terminate.")
g_p(prem = [],n = 4)
