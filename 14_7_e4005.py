n = int(input())
p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))

MAX_ROUNDS = 10**6
head1 = head2 = 0

for round_num in range(1, MAX_ROUNDS + 1):
    if head1 == len(p1):
        print("second", round_num - 1)
        break
    if head2 == len(p2):
        print("first", round_num - 1)
        break

    c1 = p1[head1]
    c2 = p2[head2]
    head1 += 1
    head2 += 1

    if (c1 > c2 and not (c1 == n - 1 and c2 == 0)) or (c1 == 0 and c2 == n - 1):
        p1.append(c1)
        p1.append(c2)
    else:
        p2.append(c1)
        p2.append(c2)

else:
    print("draw")