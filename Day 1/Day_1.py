with open('Day_1.in') as file:
    data = [i for i in file.read().split('\n')]
print(data)


sum_array = [] # sum of each chunk
total = 0 # current total of the traversal 
for item in data:
    if item == '':
        sum_array.append(total)
        total = 0
    else:
        total += int(item)

print(max(sum_array))
sum_array = sorted(sum_array)
print(sum_array[-1] + sum_array[-2] + sum_array[-3])


'''
Algorithm of the code

'''