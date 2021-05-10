#numbers list
numbers = list(input("enter the numbers seperated by commas").strip().split(","))
for index,n in enumerate(numbers):
    del numbers[index]
    numbers.insert(index, int(n))

#count of even and odd
even_count = 0
odd_count = 0
for n in numbers:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"even count is '{even_count}'\nodd count is ='{odd_count}'")
#min and max number


def min():
    min = numbers[0]
    for n in numbers:
        if min > n:
            min = n
    return min


def max():
    max = numbers[0]
    for n in numbers:
        if max < n:
            max = n
    return max

print(f"minimum value is '{min()}'")
print(f"maximum value is '{max()}'")

#FIBANOCCCCI
r_numbers = numbers[::-1]
if numbers == r_numbers:
    print("fib")
#FIBANOCCI NUMBERS IN LIST
for number in numbers:
    newnumber = str(number)
    if newnumber[::-1] == newnumber:
        print(f"{number} is fib")
