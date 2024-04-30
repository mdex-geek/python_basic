fruit = 'banana'
color = 'green'

if fruit == 'banana':
    if color == "green":
        print('unripe')
    elif color == 'yellow':
        print('ripe')
    elif color == 'brown':
        print("overripe")
else:
    print('we do not have enough data about that')