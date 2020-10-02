// This code for codechef question
try:
    t = int(input())
    for i in range(t):
        n, m, k = [int(x) for x in input().split()]
        b = []
        f = []
        for j in range(n):
            a = [int(x) for x in input().split()]
            b.append(a)
        for j in b:
            c = []
            for k in range(1, (m + 1)):
                d = 0
                for q in j:
                    if k == q:
                        d += 1
                c.append(d)
                # print(c)
            # print(".........")
            f.append(c.index(max(c)) + 1)
            # print(f)
        e = ""
        for j in f:
            e += f"{j} "
        print(e)
except:
    pass
