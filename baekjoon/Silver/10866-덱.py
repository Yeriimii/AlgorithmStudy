import sys

a = list()
n = int(sys.stdin.readline())
for _ in range(n):
    cmd = sys.stdin.readline()
    if cmd.startswith("push_b"):
        a.append(int(cmd.split()[1]))
    elif cmd.startswith("push_f"):
        a.insert(0, int(cmd.split()[1]))
    elif cmd.startswith("pop_f"):
        if len(a) == 0:
            print(-1)
        else:
            print(a.pop(0))
    elif cmd.startswith("pop_b"):
        if len(a) == 0:
            print(-1)
        else:
            print(a.pop(len(a)-1))
    elif cmd.startswith("s"):
        print(len(a))
    elif cmd.startswith("e"):
        if len(a) == 0:
            print(1)
        else:
            print(0)
    elif cmd.startswith("f"):
        if len(a) == 0:
            print(-1)
        else:
            print(a[0])
    elif cmd.startswith("b"):
        if len(a) == 0:
            print(-1)
        else:
            print(a[len(a)-1])
