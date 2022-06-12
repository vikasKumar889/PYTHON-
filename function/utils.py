import random
from secrets import choice
def generate_name():
    list1 = ['red','yellow','green','blue','orange','black','white','brown','pink']
    list2 = ['apple','banana','pineapple','mango','watermelon','cherry','strawberry','pear','grapes']
    list3 = ['cat','dog','fish','lion','tiger','bear','bird','wolf']

    p1 = random.choice(list1)
    p2 = random.choice(list2)
    p3 = random.choice(list3)
    return f'{p1}-{p2}-{p3}'