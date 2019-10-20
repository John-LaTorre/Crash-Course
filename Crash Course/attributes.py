from random import randint
class Die():
    def __init__(self, sides):
        self.sides = sides;
    def roll_die(self):
        max = self.sides;
        result = randint(1, max);
        return(result);

d6 = Die(6);
rolls = 1;
while rolls <= 6:
    attributes = [];
    for x in range(0, 4):
        result = d6.roll_die();
        attributes.append(result);
    attributes.remove(min(attributes));
    total = 0;
    for roll in attributes:
        total += roll;
    print(total);
    rolls += 1;

