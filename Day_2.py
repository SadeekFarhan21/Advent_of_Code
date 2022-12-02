with open("Day_2.in") as file:
    data = [i for i in file.read().strip().split("\n")]

total = 0
print(data)

for i, item in enumerate(data):
    item = item.replace("X", "A")
    item = item.replace("Y", "B")
    item = item.replace("Z", "C")
    print(i, item)
    # total = 0
    if item[0] == 'A': # Computer --> Rock
        # print('Rock')
        if item[1] == 'A':
            total += 1 # Player chose Rock
            total += 3 # Draw (Rock == Rock)  
        if item[1] == 'B':
            total += 2 # Player chose Paper
            total += 6 # Win (Rock < Paper)
        if item[1] == 'C':
            total += 3 # Player chose Scissors
            total += 1 # Lose (Rock > Scissors)
        # print('total:', total)
        # print('Total: ', total)
    
    
    if item[0] == 'B': # Computer --> Paper
        # print('Scissors') 
        if item[1] == 'A':
            total += 1 # Player chose Rock
            total += 1 # Lose (Paper > Rock)
        if item[1] == 'B':
            total += 2 # Player chose Paper
            total += 3 # Draw (Paper == Paper)
        if item[1] == 'C':
            total += 3 # Player chose Scissors
            total += 6 # Win (Paper < Scissors)
        # print('total:', total)
        # print('Total: ', total)

    

    if item[0] == 'C': # Computer --> Scissors
        # print('Scissors')
        if item[1] == 'A':
            total += 1 # Player chose Rock
            total += 6 # Win (Scissors < Rock) 
        if item[1] == 'B':
            total += 2 # Player chose Paper
            total += 1 # Lose (Scissors > Paper)
        if item[1] == 'C':
            total += 3 # Player chose Scissors
            total += 3 # Equal (Scissors == Scissors)
        # print('Scissors')
        # print('total:', total)
        # print('Total: ', total)
    
    # print(item[0], item[1])
print(total)