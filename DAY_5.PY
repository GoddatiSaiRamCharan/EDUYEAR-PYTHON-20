#From Range n to m all numbers divisible by 5 and 7 both
n = int(input("enter the start range variable: ").strip())
m = int(input("enter the end range variable: ").strip())
for i in range(n, m):
    if i % 5 == 0 and i % 7 == 0:
        print(i, end=" ")

#sum of series 2+22+222+....n terms
n_terms = int(input("enter the range of terms: ").strip())
series_digit = 2
sum = 0
for i in range(1, n_terms+1):
    series_digit = str(series_digit)
    sum = sum + int(series_digit*i)
print(sum)

#WHILE LOOP USE
value = input("enter the value")
sum = 0
while value != "q":
    sum += int(value)
    print("press 'q' if you want to quit ")
    value = input("enter the value")
print(sum)

#FACTORIAL
factorial_num = int(input("enter the number to find factorial"))
fact = 1
for i in range(1, factorial_num+1):
    fact = fact * i
print(fact)

# python language is best
spell = input("enter sentence: ")
n_spell = ""
for index, word in enumerate(spell):
    if index % 2 == 0:
        word = word.upper()
    n_spell = n_spell + word
nspell = n_spell.split(" ")
for word in nspell:
    word = "-".join(word)
    print(word, end=" ")