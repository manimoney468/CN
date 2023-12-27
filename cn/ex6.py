class Full:
    def _init_(self):
        self.line = ''
        self.dest = ''
        self.hops = 0

f = [Full() for _ in range(20)]

nv = int(input("Enter number of vertices: "))
sv = input("Enter source vertex: ")

print(f"Enter full table for source vertex {sv}")
for i in range(nv):
    f[i].dest, f[i].line, f[i].hops = input().split()
    f[i].hops = int(f[i].hops)

print("HIERARCHICAL TABLE")
i = 0
while i < nv:
    if sv[0] == f[i].dest[0]:
        print(f"{f[i].dest} {f[i].line} {f[i].hops}")
        i += 1
    else:
        min_hops = 1000
        minver = 0
        temp = f[i].dest[0]
        while i < nv and temp == f[i].dest[0]:
            if f[i].hops < min_hops:
                minver = i
                min_hops = f[i].hops
            i += 1
        print(f"{temp} {f[minver].line} {f[minver].hops}")
print()

'''
OUTPUT:


Enter number of vertices: 4
Enter source vertex: 1a
Enter full table for source vertex 1a
1a 0 0
1b 1c 2
1c 1d 4
1a 1d 5
HIERARCHICAL TABLE
1a 0 0
1b 1c 2
1c 1d 4
1a 1d 5'''