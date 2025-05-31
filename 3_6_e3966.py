n = int(input())
collection = list(map(int, input().split()))
m = int(input())
queries = list(map(int, input().split()))

butterfly_set = {}
for num in collection:
    butterfly_set[num] = True

for i in queries:
    if i in butterfly_set:
        print("YES")
    else:
        print("NO")