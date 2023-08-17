days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

# for i in range(len(days)):
#     print(days[i], fruite[i], drinks[i])

for day, fruite, drink in zip(days, fruits, drinks):
    print(day, fruite, drink)
