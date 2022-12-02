with open("Day_2_Challenge_1.in") as file:
    data = [i for i in file.read().strip().split("\n")]

total = 0
# print(data)

for i, item in enumerate(data):
    item = item.replace("X", "A")
    item = item.replace("Y", "B")
    item = item.replace("Z", "C")
    # print(i, item)
    points = 0
    if item[0] == 'A': # Computer --> Rock
        if item[2] == 'A':
            points += 1 # Player chose Rock
            points += 3 # Draw (Rock == Rock)  
        if item[2] == 'B':
            points += 2 # Player chose Paper
            points += 6 # Win (Rock < Paper)
        if item[2] == 'C':
            points += 3 # Player chose Scissors
            points += 0 # Lose (Rock > Scissors)

        total += points
        # print(points)
    
    if item[0] == 'B': # Computer --> Paper
        if item[2] == 'A':
            points += 1 # Player chose Rock
            points += 0 # Lose (Paper > Rock)
        if item[2] == 'B':
            points += 2 # Player chose Paper
            points += 3 # Draw (Paper == Paper)
        if item[2] == 'C':
            points += 3 # Player chose Scissors
            points += 6 # Win (Paper < Scissors)
        
        total += points
        # print(points)

    if item[0] == 'C': # Computer --> Scissors
        if item[2] == 'A':
            points += 1 # Player chose Rock
            points += 6 # Win (Scissors < Rock) 
        if item[2] == 'B':
            points += 2 # Player chose Paper
            points += 0 # Lose (Scissors > Paper)
        if item[2] == 'C':
            points += 3 # Player chose Scissors
            points += 3 # Draw (Scissors == Scissors)
    # print(item[0], item[2], item[2])
        total += points
        # print(points)
print(total)