with open('Day_6.in') as file:
    string_list = [i for i in file.read().split('\n')[0]]
for i in range(len(string_list) - 14):
    if len(list(set(string_list[i: i + 14]))) == 14:
        print(i + 14)
        break