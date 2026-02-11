#for loop

numbers = [1,2,[5,6,7],8]

for number in numbers:
    print(number)

for i in range(0,4): #(start,gap,end+1)
    print(numbers[i])

numbers = [[1,2],[5,6,7],[8]]
for number in numbers:
    for num in number:
        print(num)

