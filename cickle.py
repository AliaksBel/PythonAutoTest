#Задача: "угадай число"
start = int(input("Input start: "))
end = int(input("Input end: "))
if start > end:
    start, end = end, start
summa = 0
while start <= end:
    summa += start
    start += 1
word = input("Input word: ")
for letter in word:
    if letter == "a":
        continue
    if letter == "x":
        break
    print (letter)
else:
    print("No 'x' found")
     
print (summa)
