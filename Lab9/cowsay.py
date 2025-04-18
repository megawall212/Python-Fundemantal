import sys
import os
import heifer_generator as HeiferGenerator
from dragon import Dragon


#i = IceDragon('icedragon', IceDragon)
#f = Dragon(IceDragon, Dragon)

def list_cows(cows):
    for cow in cows:
        print(cow.get_name(), end=" ")
    print()

def find_cow(name, cows):
    for cow in cows:
        if cow.get_name() == name:
            return cow
    return None

if __name__ == '__main__':
    cows = HeiferGenerator.get_cows()
    #icedrag = i.can_breathe_fire()
    #firedrag = f.can_breathe_fire()
    args = sys.argv
    if args[1] == '-l':
        print("Cows available: ", end="")
        list_cows(cows)
    elif args[1] == '-n':
        cowname = args[2]
        cowobject = find_cow(cowname, cows)
        if cowobject == None:
            print(f'Could not find {cowname} cow!')
        else:
            for x in args[3:]:
                print(x, end=' ')
            print()
            print(cowobject.get_image())
        if isinstance(cowobject, Dragon):
            if cowobject.can_breath_fire():
                print("This dragon can breathe fire.")
            else:
                print("This dragon cannot breathe fire.")
    else:
        for x in args[1:]:
            print(x, end=" ")
        print()
        print(cows[0].get_image())
