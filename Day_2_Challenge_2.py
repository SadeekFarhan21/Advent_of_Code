with open("Day_2_Challenge_2.in") as file:
    data = [i for i in file.read().strip().split("\n")]
total = 0
for item in data:
    if item[2] == 'X': # Lose
        total += 0
        if item[0] == 'A': # Rock
            total += 3 # Scissors
        if item[0] == 'B': # Paper
            total += 1 # Rock
        if item[0] == 'C': # Scissors
            total += 2 # Paper
    if item[2] == 'Y': # Draw
        total += 3
        if item[0] == 'A': # Rock
            total += 1 # Rock
        if item[0] == 'B': # Paper
            total += 2 # Paper
        if item[0] == 'C': # Scissors
            total += 3 # Scissors
        
    if item[2] == 'Z': # Win
        total += 6
        if item[0] == 'A': # Rock
            total += 2 # Paper
        if item[0] == 'B': # Paper
            total += 3 # Scissors
        if item[0] == 'C': # Scissors
            total += 1 # Rock
    # print(item[0], item[1], item[2])
print(total)