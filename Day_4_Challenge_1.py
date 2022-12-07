with open('Day_4_Challenge_1.in') as file:
    string_list = [i for i in file.read().strip().split('\n')]
count = 0
for i in string_list:
        List = i.split(',')
        interval = List[0].strip().split('-') # Where to find
        given = List[1].strip().split('-')  # What to find
        lower_limit = int(interval[0]) # Lower limit of where to find
        upper_limit = int(interval[1]) # Upper limit of where to find
        given_lower = int(given[0]) # Lower limit of what to find
        given_higher = int(given[1]) # Upper limit of what to find
        '''
        print(interval, given) # Printing out the list
        print(lower_limit, upper_limit)
        print(given_lower, given_higher)
        '''
        if((lower_limit <= given_lower and upper_limit >= given_higher)): # or (lower_limit >= given_lower and upper_limit <= given_higher)):
            # print(lower_limit, upper_limit, given_lower, given_higher)
            count += 1    
print(count)