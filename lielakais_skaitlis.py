print("Ievadi a:")
a = int(input())
print("Ievadi b:")
b = int(input())
print("Ievadi c:")
c = int(input())
if a > b and a > c:
    print("a ir lielaks neka b un c")
elif b > a and b > c:
    print("b ir lielaks neka a un c")
else:
    print("c ir lielaks neka a un b")