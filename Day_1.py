with open('Day_1.in') as file:
    data = [i for i in file.read().split('\n')]

sum_array = [] # sum of each chunk
total = 0 # current total of the traversal 
for item in data:
    if item == '': # chunk ends
        sum_array.append(total) # appends the current total to the list
        total = 0 # resets the sum
    else:
        total += int(item) # adds the integer value of the item to total

print(max(sum_array)) # max of the whole list
sum_array = sorted(sum_array) # sorts the list
print(sum_array[-1] + sum_array[-2] + sum_array[-3]) # sum of three highest values


'''
Algorithm of the code

1. First opens up the file in the form of Day_1.in
2. Reads and splits up the dataset filled with numbers based on new line and puts is a list
3. Take a variable(total) to keep track of current traversing total for the list and a list(sum_array) to keep all the totals
4. Keep adding int(item) aka number until find an empty string which means its the end of that chunk
5. Append the total to the list (sum_array)
6. Use max(list) function to get the max value of the array (First Answer)
7. Sort the array descending and the get last 3 values (Second Answer) 

'''