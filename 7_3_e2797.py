n = int(input())
numbers = input().split()

phone_book = set()

for number in numbers:
    phone_book.add(number)

print(len(phone_book))