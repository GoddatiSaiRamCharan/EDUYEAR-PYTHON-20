#INDEX VALUES FOR VOWELS
word = list(input("enter the string").strip().lower())
for index, letter in enumerate(word):
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == "o" or letter == "u":
        print(f"{index}", end="\t")

#reverse word of string
sentence = input("enter the sentence").strip()
sentence = sentence.split(" ")
n_sentence = []
for word in sentence[::-1]:
    n_sentence.append(word)
n_sentence = (" ").join(n_sentence)
print(n_sentence)

#remove duplicates without set()
numberslist = []
numbers = input("enter the numbers seperated by commas").strip().split(",")
for index, number in enumerate(numbers):
    if index == 0:
        numberslist.append(int(number))
    else:
        for n in numberslist:
            if n == int(number):
                break
        else:
            numberslist.append(int(number))
print(numberslist)
