d = {"beauty": True, "truth": True, "red wheelbarrow": 100000, 5: "fingers"}
for key in d:
    print(key)

for val in d.values():
    print(val)


numbers = [3, 9, 1, 5, 7, 2, 11, 0, 3, 12, 3, 15]
# using control flows to find the largest value in the number
temp_largest = numbers[0]
print('Before', temp_largest)

for number in numbers:
    #compare with each number then giving the larger value
    if number > temp_largest:
        temp_largest = number
        print(number, temp_largest)
print(f'The largest value is {temp_largest}')

for i in range(1,4):
    for j in range(1,4):
        if i <= j:
            print(i,j)


for even in range(0,10,2):
    print(even)
    if even >2:
        break


for odd in range(1,10,2):
    for even in range(0,10,2):
        if even > 2:
            break
    print(even,odd)


for even in range(0,10,2):
    print(even)
    if even > 2:
        continue

for even in range(0,10,2):
    if even > 2:
        continue
print(even)